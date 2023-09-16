<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;
</script>

{#if data}
	<section class="card m-4 shadow-xl bg-primary">
		<div class="card-body">
			<h2 class="card-title">{data.name}</h2>
		</div>
	</section>
{:else}
	<span class="loading loading-spinner loading-lg" />
{/if}
