
<!-- [ SCRIPT ] -->
<script>

    // [ IMPORTS: components ]
    import { fade } from 'svelte/transition'

</script>


<!-- [ TEMPLATE: Documents ] -->
<svelte:head>
    <title>Documents</title>
</svelte:head>

<main in:fade='{{ duration: 100 }}' out:fade|local='{{ duration: 100 }}' class = 'documents'>
    <h1>Documents page</h1>
</main>
