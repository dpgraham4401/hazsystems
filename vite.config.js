import {ConfigEnv, defineConfig, loadEnv} from "vite";

const {resolve} = require("path");

export default defineConfig((envConfig) => {
    const env = loadEnv(envConfig.mode, process.cwd(), '');
    return {
        plugins: [],
        root: resolve('./static/src'),
        base: '/static/',
        server: {
            host: env.DJANGO_VITE_DEV_SERVER_HOST,
            port: env.DJANGO_VITE_DEV_SERVER_PORT,
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
            manifest: "manifest.json",
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
    }
})