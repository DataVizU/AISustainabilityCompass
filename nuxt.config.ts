// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app: {
    head: {
      title: "AI Sustainability Compass",
      link: [{ rel: "icon", type: "image/png", href: "/favicon.png" }],
      htmlAttrs: {
        lang: "en",
      },
      script: [
        {
          src: "https://api.map.baidu.com/api?v=1.0&&type=webgl&ak=fUpczAds64HUQB67oLdlvxiZxSqRors6",
        },
      ],
    },
  },
  devtools: { enabled: true },
  modules: ["@nuxtjs/eslint-module", "@nuxt/ui"],
  eslint: {
    lintOnStart: false,
  },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  css: ["@/assets/css/main.css"],
  colorMode: {
    preference: "light",
  },
});
