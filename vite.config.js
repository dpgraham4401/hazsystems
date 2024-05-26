import {defineConfig} from "vite";

const {resolve} = require("path");

export default defineConfig({
    plugins: [],
    root: resolve('./static/src'),
    base: '/static/',
    server: {
        host: 'localhost',
        port: 3000,
        open: false,
        watch: {
            usePolling: true,
            disableGlobbing: false,
        },
    },
    resolve: {
        extensions: ['.js', '.json'],
    },
    build: {
        outDir: resolve('./static/dist'),
        assetsDir: '',
        manifest: true,
        emptyOutDir: true,
        target: 'es2015',
        rollupOptions: {
            input: {
                main: resolve('./static/src/js/hello.js'),
            },
            output: {
                chunkFileNames: undefined,
            },
        },
    },
})