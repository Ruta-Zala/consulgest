module.exports = {
	content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
	theme: {
		extend: {
			fontFamily: {
				sans: ['Poppins', 'sans-serif'],
			},
			colors: {
				'c-blue': '#03579A',
				'c-deep-blue': '#072EF5',
				'c-dark-blue': '#333984',
				'c-dark': '#181C54',
				'c-polo-blue': '#92AAD7',
				'c-coral-blue': '#C4D6F7',
				'c-warning': '#EC7E0E',
				'c-light-orange': '#F6A44F',
				'c-success': '#2AD7B3',
				'c-grey': '#C4D6F6',
				'c-light-grey': '#889DC6',
				'c-ghost-white': '#F9F9FF',
				'c-input-grey': '#C4D6F7',
				'c-pink': '#FF005C',
				'c-purple': '#A955EB',
				'c-vivid-green': '#0DE4E4',
				'c-charts-bg': '#F1F6FF',
				'c-grey-bg': '#F8F8FF',
				'c-error': '#FF2D2D',
			},
			boxShadow: {
				'3xl': '0 10px 20px rgba(43, 94, 224, 0.12)',
				'2xl': '0 60px 80px rgba(43, 94, 224, 0.2)',
				'xl': '0 10px 20px rgba(43, 94, 224, 0.2)',
				'l': '0 8px 20px rgba(70, 128, 255, 0.16)',
				'sm': '0 35px 50px rgba(96, 150, 249, 0.23)',
			},
			backgroundImage: {
				'c-linear': 'linear-gradient(0deg, #F9F9FF, #F9F9FF)',
				'c-linear-orizon':
					'linear-gradient(270deg, #557CFF 0%, #7368FF 49.72%, #9F55FE 100%);',
				'c-linear-blue':
					'linear-gradient(280.17deg, #0647CA 24.69%, #0175FD 100%)',
			},
			dropShadow: {
				sm: '0 10px 17px rgba(77, 112, 246, 0.24)',
			},
		},
	},
	plugins: [require('daisyui')],
	daisyui: {
		themes: [
			{
				light: {
					'primary': '#333984',
					'primary-focus': '#333984',
					'primary-content': '#ffffff',
					'secondary': '#2AD7B3',
					'secondary-focus': '#2AD7B3',
					'secondary-content': '#ffffff',
				},
			},
		],
	},
};
