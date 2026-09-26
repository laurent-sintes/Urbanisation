import { chromium } from 'playwright';
export { chromium };
export const browserOptions = { headless: true, ...(process.env.ATLAS_BROWSER_CHANNEL ? { channel: process.env.ATLAS_BROWSER_CHANNEL } : {}) };
