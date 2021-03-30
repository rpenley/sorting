function updateData(chart, data) {
    //chart.data.labels.push(label);
    chart.data.datasets[0].data = data;
    chart.update();
}

function removeData(chart) {
    chart.data.labels.pop();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.pop();
    });
    chart.update();
}

function getRandomData(size, range) {
data = [];	
	for(i=0; i<size; i++){
		data[i] = Math.floor(Math.random() * Math.floor(range));
	}
return data;
}

function bubbleSort(chart, data) {
    var length = data.length;
    //Number of passes
    for (var i = 0; i < length; i++) { 
        //Notice that j < (length - i)
        for (var j = 0; j < (length - i - 1); j++) { 
            //Compare the adjacent positions
            if(data[j] > data[j+1]) {
                //Swap the numbers
                var tmp = data[j];  //Temporary variable to hold the current number
                data[j] = data[j+1]; //Replace current number with adjacent number
                data[j+1] = tmp; //Replace adjacent number with current number
								updateData(chart, data);
								console.log(data);
            }
        }        
    }
}

function genLables(data) {
size = data.length;
labels = [];
for (i=0; i<size; i++) {
	labels[i] = data[i].toString();
}
return labels;
}

function createChart(data, labels){
var ctx = document.getElementById('barChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
				labels: labels,
        datasets: [{
            label: 'Sort Data',
            backgroundColor: 'rgb(255, 99, 132)',
						barPercentage: 1,
            borderColor: 'rgb(255, 99, 132)',
            data: data,
        }]
    },

    // Configuration options go here
    options: {
        animation: {
            duration: 0 // general animation time
        },
        hover: {
            animationDuration: 0 // duration of animations when hovering an item
        },
        responsiveAnimationDuration: 0 // animation duration after a resize	
		}
});
return chart;
}

//console.log(chart.data.datasets[0].data);
var data = getRandomData(20, 50);
var labels = genLables(data);
console.log(data);
chart = createChart(data, labels); 
//removeData(chart);
//updateData(chart, data);
bubbleSort(chart, data);
