
<!-- [ SCRIPTS ] -->
<script>

    // [ IMPORTS: system ]
    import { fade } from 'svelte/transition';
    import { onMount } from 'svelte';

    // [ PROPS ]
    const script = [2000, 8000, 2000, 4000, 2800];
    const sched  = [ 
        ['07:35', 'Ожидается груз ...'] ,
        ['09:20', 'Прибыло на место разгрузки груза'] ,
        ['09:25', 'Производится разгрузка'] ,
        ['10:40', 'Отправлено на производство'] ,
        ['11:00', 'Работа окончена'] ,
    ];


    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    function renderSched(process, ul) {
        let li    = document.createElement('li')
        let time  = document.createElement('span')
        let descr = document.createElement('span')

        time.textContent  = process[0]
        descr.textContent = process[1]

        li.setAttribute('class', 'sched-row active')
        time.setAttribute('class', 'time')
        descr.setAttribute('class', 'descr')

        li.appendChild(time)
        li.appendChild(descr)
        ul.prepend(li)
    }

    function clearActiveProcess() {
        let actives = document.querySelectorAll('.sched-row.active');
        actives.forEach(a => {
            a.classList.remove('active')
        })
    }

    onMount(() => {
        let ul = document.querySelector('.process-schedule ul') 
        for(let process of sched) {
            clearActiveProcess();
            renderSched(process, ul);
        }
    });


</script>


<!-- [ TEMPLATE ] -->
<div class="process-schedule">
    <p class = 'caption'>Текущее состояние:</p>
    <ul>
    </ul>
</div>