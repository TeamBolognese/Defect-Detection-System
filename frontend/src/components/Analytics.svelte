
<!-- [ SCRIPTS ] -->
<script>

    // [ PROPS ]
    export let analytics;

</script>


<!-- [ TEMPLATE ] -->
<div class="analytics">
    <p class = 'caption'>Анализ качества груза:</p>
    {#if analytics.defects}
        <p class = 'estimation defect'>Обнаружен брак</p>
    {:else}
        <p class = 'estimation no-defect'>Брак не обнаружен</p>
    {/if}


    <div class="defect-rate">
        <!-- <img src="/img/circle-progress.png" alt="defect-rate"> -->
        <canvas class = 'progress' value = { analytics.defect_rate }></canvas>
        <span class="caption">Процент брака</span>
    </div>

    <p class="invoice">{ '₽ ' + analytics.invoice }</p>
</div>