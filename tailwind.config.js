/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/*.{php,js,html}",
    "./*.{php,js,html}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#202225",
        secondary: "#5865f2",
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
