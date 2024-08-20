let tokenCount = 0.00000;
let setNulTocen = 0.00000;
const increment = 0.00001;
let name_start = "start";
let Click_start_Farm = 0;

const element = document.getElementById('yourElementId');
const counterElement = document.getElementById('Counter-WATT');

if (element && counterElement) {
    element.textContent = name_start;

    function startFarm() {
        Click_start_Farm++;
        if (Click_start_Farm === 1) {
            setInterval(() => {
                tokenCount += increment;
                element.textContent = tokenCount.toFixed(5) + " WATT";
            }, 1000);
        }
    }

    function handleClick() {
        setNulTocen += tokenCount;
        counterElement.textContent = setNulTocen.toFixed(5) + " WATT";
        tokenCount *=0; 
    }

    element.addEventListener('click', startFarm);
    element.addEventListener('click', handleClick);
} else {
    console.log('Element(s) not found');
}
