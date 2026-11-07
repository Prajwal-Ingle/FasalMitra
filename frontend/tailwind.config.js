/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'neo-canvas': '#FFFDF7',
        'neo-blue': '#D9EBF5',
        'neo-dark': '#1E293B',
        'neo-green': '#22C55E',
        'neo-green-dark': '#16A34A',
        'neo-pastel-mint': '#DCFCE7',
        'neo-pastel-blue': '#BAE6FD',
        'neo-pastel-coral': '#FED7AA',
        'neo-pastel-pink': '#FCE7F3',
        'neo-pastel-yellow': '#FEF08A',
      },
      boxShadow: {
        'neo-sm': '2px 2px 0px #1E293B',
        'neo': '4px 4px 0px #1E293B',
        'neo-lg': '6px 6px 0px #1E293B',
      }
    },
  },
  plugins: [],
}
