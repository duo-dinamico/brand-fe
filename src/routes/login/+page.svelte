<script lang="ts">
	let username = '';
	let password = '';
	let error: string | null = null;
	const handleSubmit = async () => {
		try {
			const response = await fetch('https://brands.duodinamico.online/login/', {
				method: 'POST',
				headers: {
					origin: '*'
				},
				body: JSON.stringify({ username, password })
			});

			if (!response.ok) {
				throw new Error('Authentication failed');
			}
		} catch (err) {
			error = err.message;
		}
	};
</script>

{#if error}
	<p>{error}</p>
{/if}

<form on:submit={handleSubmit}>
	<input
		type="text"
		placeholder="Enter your email"
		class="input input-bordered w-full max-w-xs"
		bind:value={username}
		required
	/>
	<input
		type="password"
		placeholder="Enter your password"
		class="input input-bordered w-full max-w-xs"
		bind:value={password}
		required
	/>
	<input type="submit" value="Login" class="btn" />
</form>
