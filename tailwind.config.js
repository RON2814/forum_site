/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./forum/templates/**/*.html",
    "./post/templates/**/*.html",
    "./user/templates/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        lightBg: "hsl(0, 0%, 96%)",
      },
    },
  },
  plugins: [],
};
