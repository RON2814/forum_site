/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./forums/templates/**/*.html",
    "./posts/templates/**/*.html",
    "./users/templates/**/*.html",
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
