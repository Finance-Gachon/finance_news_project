import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Chart, Doughnut } from 'react-chartjs-2';
import ChartDataLabels from 'chartjs-plugin-datalabels'
ChartJS.register(ArcElement, Tooltip, Legend);
 
function DoughnutChart(props) {
    const sentimentData = props.data;
    const positiveSum = sentimentData.reduce((sum, data) => sum + data.positive, 0);
    const neutralSum = sentimentData.reduce((sum, data) => sum + data.neutral, 0);
    const negativeSum = sentimentData.reduce((sum, data) => sum + data.negative, 0);
    
    const options = {
        responsive: true,
        plugins: {
            // Change options for ALL labels of THIS CHART
            datalabels: {
                formatter: (value, ctx) => {
                    let sum = 0;
                    let dataArr = ctx.chart.data.datasets[0].data;
                    dataArr.map(data => {
                        sum += data;
                    });
                    let percentage = (value*100 / sum).toFixed(2)+"%";
                    return percentage;
                },
                color: '#000000',
                align: 'center',
            },
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "긍 · 부정 비율",
            },
        },
    };

    const data = {
        labels: ['긍정', '중립', '부정'],
        datasets: [
          {
            label: "건수",
            // data: [positiveSum / totalSum, neutralSum / totalSum, negativeSum / totalSum],
            data: [positiveSum, neutralSum, negativeSum],
            backgroundColor: [
                "rgba(63, 102, 218, 0.5)",
                "rgba(251, 196, 0, 0.5)",
                "rgba(255, 74, 111, 0.5)",
            ],
            borderColor: [
                "rgba(63, 102, 218, 1)",
                "rgba(251, 196, 0, 1)",
                "rgba(255, 74, 111, 1)",
            ],
            borderWidth: 1,
          },
        ],
      };
    
    
    return (
        <div style={{width:'400px'}}>
            {sentimentData.length > 0 && <Doughnut options={options} plugins={[ChartDataLabels]} data={data} />}
        </div>
    );
}
 
export default DoughnutChart;