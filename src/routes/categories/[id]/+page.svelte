<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';

	let category: any;

	onMount(() => {
		fetch(`https://brands.duodinamico.online/categories/${$page.params.id}`)
			.then((response) => response.json())
			.then((result) => (category = result.categories[0]));
	});
</script>

{#if category}
	<section class="card m-4 shadow-xl bg-primary">
		<div class="card-body">
			<h2 class="card-title">{category.name}</h2>
		</div>
	</section>
{:else}
	<span class="loading loading-spinner loading-lg" />
{/if}
