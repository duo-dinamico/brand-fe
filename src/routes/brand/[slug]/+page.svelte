<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';

	let brand;

	onMount(() => {
		fetch(`https://brands.duodinamico.online/brands/${$page.params.slug}`)
			.then((response) => response.json())
			.then((result) => (brand = result.brands[0]));
	});
</script>

{#if brand}
	<div class="card w-2/3 shadow-xl bg-primary">
		<div class="card-body">
			<h2 class="card-title">{brand.name}</h2>
			<p>{brand.description}</p>
			<div class="card-actions justify-end">
				<button class="btn btn-secondary"
					><a href="/categories/{brand.category.id}">{brand.category.name}</a></button
				>
			</div>
		</div>
	</div>
{:else}
	<span class="loading loading-spinner loading-sm" />
{/if}
