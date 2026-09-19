import unittest
from scripts.test_publish_release import isolated_project
from scripts.verification_checkpoint import run


class VerificationCheckpointTests(unittest.TestCase):
    def test_content_code_output_and_inventory_changes_force_replay(self):
        with isolated_project() as root:
            cache = root/'cache.json'
            data, code, output = [root/name for name in ('model.yaml', 'verify.py', 'view.md')]
            data.write_text('a', encoding='utf-8')
            code.write_text('b', encoding='utf-8')
            calls = []
            def action():
                calls.append(True)
                output.write_text('view', encoding='utf-8')
                return {'status': 'passed'}
            def paths():
                return [p for p in root.iterdir() if p != cache]
            def check(full=False):
                return run(cache, paths, action, [output], full=full)[1]
            self.assertFalse(check())
            self.assertTrue(check())
            data.write_text('z', encoding='utf-8')
            self.assertFalse(check())
            code.write_text('c', encoding='utf-8')
            self.assertFalse(check())
            output.unlink()
            self.assertFalse(check())
            (root/'new-input').write_text('new', encoding='utf-8')
            self.assertFalse(check())
            self.assertFalse(check(full=True))
            self.assertTrue(check())
            self.assertEqual(len(calls), 6)

    def test_failure_and_concurrent_input_changes_never_leave_success_cached(self):
        with isolated_project() as root:
            data = root/'input'
            data.write_text('before', encoding='utf-8')
            cache = root/'cache.json'
            run(cache, lambda: [data], lambda: {'status': 'passed'}, [])
            def failure():
                raise ValueError('invalid proof')
            with self.assertRaisesRegex(ValueError, 'invalid proof'):
                run(cache, lambda: [data], failure, [], full=True)
            self.assertFalse(cache.exists())
            def changing():
                data.write_text('after', encoding='utf-8')
                return {'status': 'passed'}
            with self.assertRaisesRegex(ValueError, 'inputs changed'):
                run(cache, lambda: [data], changing, [])
            self.assertFalse(cache.exists())

    def test_invalid_checkpoint_falls_back_to_full_verification(self):
        with isolated_project() as root:
            cache = root/'cache.json'
            cache.write_text('{invalid', encoding='utf-8')
            result, reused = run(cache, lambda: [], lambda: {'status': 'passed'}, [])
            self.assertEqual(result['status'], 'passed')
            self.assertFalse(reused)
