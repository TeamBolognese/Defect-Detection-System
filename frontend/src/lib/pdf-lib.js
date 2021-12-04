
// [ IMPORTS ]
import { TYPO, pages } from './pdf-pages.js';

// [ FUNCTIONS ]

//@ create > new PDF doc
// const FONTS = {
//     helveticaFont: PDFLib.PDFFont.embed('Helvetica'),
// }

export async function createPDF() {

    // define > doc settings
    const DOC_SETTINGS = {
        size:       [210, 290],
        page_pad:   [25, 21],
        offset:     [25, 290 - 21]
    }

    // create PDF doc instance
    const doc = await PDFLib.PDFDocument.create()
    // const timesRomanFont = await doc.embedFont(StandardFonts.TimesRoman)

    // loop > through all pages | render > content
    pages.forEach(page => {

        // create > page
        const sheet = doc.addPage(DOC_SETTINGS.size);
        
        // render > content
        page.forEach(async (section) => {

            const { type, separator, pad_top, pad_bottom, style, txt } = section;

            if( type == 'img' ) {

                let img_buff = await fetch(section?.src).then((res) => res.arrayBuffer())
                let img = await doc.embedJpg(img_buff)
                let img_scale = img.scale(0.5)
                sheet.drawImage(img, {
                    // x: DOC_SETTINGS.offset[0], y: DOC_SETTINGS.offset[1] - pad_top,
                    x: 5, y: 5,
                    opacity: 1,
                    width: img_scale.width, height: img_scale.height,
                })

            } else {

                //? if > top separator used
                if( separator == 'top' ) {
                    sheet.drawLine({
                        thickness: 0.5,
                        start: { x: DOC_SETTINGS.offset[0], y: DOC_SETTINGS.offset[1] - pad_top + 5 },
                        end: { x: DOC_SETTINGS.size[0] - DOC_SETTINGS.page_pad[0], y: DOC_SETTINGS.offset[1] - pad_top + 5 },
                    });
                    DOC_SETTINGS.offset[1] -= 5;
                }

                // render > page content
                sheet.drawText(txt, {
                    x: DOC_SETTINGS.offset[0], y: DOC_SETTINGS.offset[1] - pad_top,
                    //font:  style.font,
                    size:  style.size,
                    lineHeight: 8,
                    maxWidth: DOC_SETTINGS.size[0] - DOC_SETTINGS.page_pad[0] * 2,
                    //color: color.size,
                })

                //? if > bottom separator used
                if( separator == 'bottom' ) {
                    sheet.drawLine({
                        thickness: 0.5,
                        start: { x: DOC_SETTINGS.offset[0], y: DOC_SETTINGS.offset[1] - pad_top - 5 },
                        end: { x: DOC_SETTINGS.size[0] - DOC_SETTINGS.page_pad[0], y: DOC_SETTINGS.offset[1] - pad_top - 5 },
                    });
                    DOC_SETTINGS.offset[1] -= 5;
                }

                // keep > current X offset (for next section)
                DOC_SETTINGS.offset[1] -= pad_top + pad_bottom

            }

        })

    });

    // save > doc | prepare > view link
    const link = document.querySelector('.view-pdf');
    const uri = await doc.saveAsBase64({ dataUri: true })
    link.href = uri

    return false;

}

export function openPDF( e ) {
    console.log(e);
    const uri = e.target.href;
    let win = window.open();
    win.document.write('<iframe src="' + uri  + '" frameborder="0" style="border:0; top:0px; left:0px; bottom:0px; right:0px; width:100%; height:100%;" allowfullscreen></iframe>');
}




