<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;

	const { brand, brandSocials } = data;
</script>

{#if data}
	<section class="card m-4 shadow-xl bg-primary">
		<div class="card-body">
			<h2 class="card-title">{brand.name}</h2>
			<p>Description: {brand.description}</p>
			<p>Average price: {brand.average_price}</p>
			<details class="collapse collapse-arrow border border-base-300 bg-base-200">
				<summary class="collapse-title">Socials</summary>
				<div class="collapse-content">
					{#each brandSocials as brandSocial (brandSocial.id)}
						<p>{brandSocial.social.name}</p>
						<p>{brandSocial.address}</p>
					{/each}
				</div>
			</details>
			<details class="collapse collapse-arrow border border-base-300 bg-base-200">
				<summary class="collapse-title">Address</summary>
				<div class="collapse-content">
					<p>{brand.line_address_1}</p>
					<p>{brand.line_address_2}</p>
					<p>{brand.city}</p>
					<p>{brand.postal_code}</p>
				</div>
			</details>
			<div class="card-actions justify-end">
				<a role="button" class="btn btn-sm" href="/categories/{brand.category.id}"
					>{brand.category.name}</a
				>
			</div>
		</div>
	</section>
{:else}
	<span class="loading loading-spinner loading-lg" />
{/if}
