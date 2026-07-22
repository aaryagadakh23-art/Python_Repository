import { defineConfig } from "vite";

export default defineConfig({
    server: {
        host: true,
        port: 3000
    },

    preview: {
        port: 4173
    }
});