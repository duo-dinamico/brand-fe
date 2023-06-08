<script lang="ts">
  const addBrand = () => {
    alert("Can't add Brand yet.");
  };
</script>

<footer class="absolute inset-x-0 bottom-0 h-16">
  <button
    class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    on:click={addBrand}
  >
    addBrand
  </button>
</footer>

<style lang="postcss">
  footer {
    background-color: rgb(96, 104, 98);
  }
</style>
