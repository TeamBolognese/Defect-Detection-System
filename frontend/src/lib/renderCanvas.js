
export function renderCanvas() {
    let circles = document.querySelectorAll('canvas.progress');

    circles.forEach(circle => {
        let value = +circle.getAttribute('value');
        let percentage = value * 100 + '%';
        let ctx = circle.getContext('2d');

        // draw > percentage
        ctx.font = "18pt Montserrat";
        ctx.fillStyle  = "#C65BEC";
        ctx.fillText(percentage, circle.width / 2 - 18, circle.height / 2 + 9);

        // draw > full circle
        ctx.lineWidth = 8;
        ctx.strokeStyle = "#E2E6ED";
        ctx.beginPath();
        ctx.arc(circle.width / 2, circle.height / 2, 50, 0, 2 * Math.PI);
        ctx.stroke();

        // draw > actual value
        ctx.strokeStyle = "#C65BEC";
        ctx.beginPath();
        ctx.arc(circle.width / 2, circle.height / 2, 50, 0, (2 * value) * Math.PI);
        ctx.stroke();
    });

}