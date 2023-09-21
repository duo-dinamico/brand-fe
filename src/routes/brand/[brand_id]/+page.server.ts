import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

const fetchData = (url: string) => {
	return fetch(url)
		.then((response) => response.json())
		.then((result) => result);
};

export const load: PageServerLoad = async ({ params }) => {
	const [brand, brandSocials] = await Promise.all([
		fetchData(`https://brands.duodinamico.online/brands/${params.brand_id}`),
		fetchData(`https://brands.duodinamico.online/brands/${params.brand_id}/socials/`)
	]);

	if (brand && brandSocials) {
		return { brand: brand.brands[0], brandSocials: brandSocials.socials };
	}

	throw error(404, 'Not found');
};
