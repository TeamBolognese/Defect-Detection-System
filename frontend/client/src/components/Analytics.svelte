
<!-- [ SCRIPTS ] -->
<script>

    // [ PROPS ]
    export let analytics;

</script>


<!-- [ TEMPLATE ] -->
<div class="analytics">
    <p class = 'caption'>Анализ качества груза:</p>
    {#if analytics.status == 'bad'}
        <p class = 'estimation defect'>Обнаружен брак</p>
    {:else}
        <p class = 'estimation no-defect'>Брак не обнаружен</p>
    {/if}


    <div class="defect-rate">
        <!-- <img src="/img/circle-progress.png" alt="defect-rate"> -->
        <canvas class = 'progress' value = { analytics.percent }></canvas>
        <span class="caption">Процент брака</span>
    </div>

    <p class="invoice">счет: { '₽ ' + analytics.invoice }</p>
</div>