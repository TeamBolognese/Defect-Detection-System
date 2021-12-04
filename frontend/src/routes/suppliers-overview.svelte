
<!-- [ SCRIPT ] -->
<script>

    // [ IMPORTS: extensions ]
    import { renderCanvas } from '$lib/renderCanvas.js';


    // [ IMPORTS: components ]
    import { fade } from 'svelte/transition'
    import { onMount } from 'svelte';

    const analytics = {
        defects:     true,       // has defects / no defects
        defect_rate: 0.15,       // percentage
        invoice:     1200000,    // price of no-defect cargo
    }


    // [ HOOKS ]
    onMount(() => {
        renderCanvas();
    });

</script>


<!-- [ TEMPLATE: Monitoring ] -->
<svelte:head>
    <title>Monitoring</title>
</svelte:head>

<main in:fade='{{ duration: 100 }}' out:fade|local='{{ duration: 100 }}' class = 'suppliers-overview'>

    <!-- [ section: recommended suppliers ] -->
    <section class="recommended-suppliers suppliers">

        <!-- title -->
        <div class="title">
            <p class="title">Рекомендованные поставщики</p>
        </div>

        <!-- supplier cards -->
        <div class="supplier-cards">

            <div class="supplier-card">
                <!-- supplier info -->
                <div class="supplier-info">
                    <p class="supplier-title">
                        <span class = 'city'>г. Орел</span>
                        ООО Белкин и Стрелкин
                    </p>

                    <p class="supplier-metrics">
                        <span class = 'cargo-price'>₽ 1 200 000 / т</span>
                        <span class = 'cargo-price'><b>350 тонн</b> в наличии</span>
                        <span class = 'cargo-price'>постоплата</span>
                    </p>

                    <div class="time-badge badge">
                        3 час
                    </div>
                </div>

                <!-- supplier info -->
                <div class="defect-rate">
                    <div class="estimation">
                        <canvas class = 'progress' value = { analytics.defect_rate }></canvas>
                        <p class="caption">Процент брака</p>
                    </div>
                    <button class="CTA-small select">выбрать</button>
                </div>
            </div>

            <div class="supplier-card">
                <!-- supplier info -->
                <div class="supplier-info">
                    <p class="supplier-title">
                        <span class = 'city'>г. Орел</span>
                        ООО Белкин и Стрелкин
                    </p>

                    <p class="supplier-metrics">
                        <span class = 'cargo-price'>₽ 1 200 000 / т</span>
                        <span class = 'cargo-price'><b>350 тонн</b> в наличии</span>
                        <span class = 'cargo-price'>постоплата</span>
                    </p>

                    <div class="time-badge badge">
                        3 час
                    </div>
                </div>

                <!-- supplier info -->
                <div class="defect-rate">
                    <div class="estimation">
                        <canvas class = 'progress' value = { analytics.defect_rate }></canvas>
                        <p class="caption">Процент брака</p>
                    </div>
                    <button class="CTA-small select">выбрать</button>
                </div>
            </div>

            <div class="supplier-card">
                <!-- supplier info -->
                <div class="supplier-info">
                    <p class="supplier-title">
                        <span class = 'city'>г. Орел</span>
                        ООО Белкин и Стрелкин
                    </p>

                    <p class="supplier-metrics">
                        <span class = 'cargo-price'>₽ 1 200 000 / т</span>
                        <span class = 'cargo-price'><b>350 тонн</b> в наличии</span>
                        <span class = 'cargo-price'>постоплата</span>
                    </p>

                    <div class="time-badge badge">
                        3 час
                    </div>
                </div>

                <!-- supplier info -->
                <div class="defect-rate">
                    <div class="estimation">
                        <canvas class = 'progress' value = { analytics.defect_rate }></canvas>
                        <p class="caption">Процент брака</p>
                    </div>
                    <button class="CTA-small select">выбрать</button>
                </div>
            </div>

            <div class="supplier-card">
                <!-- supplier info -->
                <div class="supplier-info">
                    <p class="supplier-title">
                        <span class = 'city'>г. Орел</span>
                        ООО Белкин и Стрелкин
                    </p>

                    <p class="supplier-metrics">
                        <span class = 'cargo-price'>₽ 1 200 000 / т</span>
                        <span class = 'cargo-price'><b>350 тонн</b> в наличии</span>
                        <span class = 'cargo-price'>постоплата</span>
                    </p>

                    <div class="time-badge badge">
                        3 час
                    </div>
                </div>

                <!-- supplier info -->
                <div class="defect-rate">
                    <div class="estimation">
                        <canvas class = 'progress' value = { analytics.defect_rate }></canvas>
                        <p class="caption">Процент брака</p>
                    </div>
                    <button class="CTA-small select">выбрать</button>
                </div>
            </div>

        </div>

    </section>

    <!-- [ section: rest suppliers ] -->
    <section class="rest-suppliers suppliers">

        <!-- title -->
        <div class="title">
            <p class="title">Прочие поставщики</p>
        </div>

        <!-- supplier cards -->
        <div class="supplier-cards">

            <div class="supplier-card">
                <!-- supplier info -->
                <div class="supplier-info">
                    <p class="supplier-title">
                        <span class = 'city'>г. Орел</span>
                        ООО Белкин и Стрелкин
                    </p>

                    <p class="supplier-metrics">
                        <span class = 'cargo-price'>₽ 1 200 000 / т</span>
                        <span class = 'cargo-price'><b>350 тонн</b> в наличии</span>
                        <span class = 'cargo-price'>постоплата</span>
                    </p>

                    <div class="time-badge badge">
                        3 час
                    </div>
                </div>

                <!-- supplier info -->
                <div class="defect-rate">
                    <div class="estimation">
                        <canvas class = 'progress' value = { analytics.defect_rate }></canvas>
                        <p class="caption">Процент брака</p>
                    </div>
                    <button class="CTA-small select">выбрать</button>
                </div>
            </div>

            <div class="supplier-card">
                <!-- supplier info -->
                <div class="supplier-info">
                    <p class="supplier-title">
                        <span class = 'city'>г. Орел</span>
                        ООО Белкин и Стрелкин
                    </p>

                    <p class="supplier-metrics">
                        <span class = 'cargo-price'>₽ 1 200 000 / т</span>
                        <span class = 'cargo-price'><b>350 тонн</b> в наличии</span>
                        <span class = 'cargo-price'>постоплата</span>
                    </p>

                    <div class="time-badge badge">
                        3 час
                    </div>
                </div>

                <!-- supplier info -->
                <div class="defect-rate">
                    <div class="estimation">
                        <canvas class = 'progress' value = { analytics.defect_rate }></canvas>
                        <p class="caption">Процент брака</p>
                    </div>
                    <button class="CTA-small select">выбрать</button>
                </div>
            </div>

        </div>

    </section>

</main>
