
// [ SETTINGS: typography ]
export const TYPO = {
    // headings
    h1: {
        //color: rgb(0.95, 0.1, 0.1),
        //font: FONTS.helveticaFont,
        size: 13
    },
    h2: {
        //color: rgb(0.95, 0.1, 0.1),
        //font: FONTS.helveticaFont,
        size: 7
    },

    // body text
    p: {
        //color: rgb(0.95, 0.1, 0.1),
        //font: FONTS.helveticaFont,
        size: 5
    },
}

// [ PAGES CONTENT ]
export const pages = [
    // page
    [
        // content section
        { 
            type:       "h1", 
            style:      TYPO[ "h1" ],
            separator:  "none",
            pad_top:    0,
            pad_bottom: 11,
            txt:        "Invoice",
            //txt:        "Счет-фактура",
        },

        // content section
        { 
            type:       "h2", 
            style:      TYPO[ "h2" ],      // TYPO[ this.type ]
            separator:  "bottom",
            pad_top:    0,
            pad_bottom: 20,
            txt:        "Raw materials analysis report",
            // txt:        "Отчет анализа сырья",
        },

        // content section
        { 
            type:       "p", 
            style:      TYPO[ "p" ],
            separator:  "none",
            pad_top:    0,
            pad_bottom: 0,
            txt:        "According to the results the following defects were discovered: cargo is missing",
            // txt:        "По результатам анализа сырья выявлены следующие дефекты: отсутствует груз",
        },

        // content section
        { 
            type:       "img", 
            separator:  "none",
            pad_top:    0,
            pad_bottom: 0,
            src:        "../img/pony.jpg",
        },

        // content section
        { 
            type:       "p", 
            style:      TYPO[ "p" ],
            separator:  "top",
            pad_top:    50,
            pad_bottom: 0,
            txt:        "Invoice: USD 7,200"
        },
    ],
]