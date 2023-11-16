import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";
 
ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);
 

function LineChart(props) {
    const sentimentData = props.data;
    const options = {
        responsive: true,
        plugins: {
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "긍 · 부정 추이",
            },
        },
    };
 
    let labels = [];
    if (sentimentData.length > 0) {
        labels = sentimentData.map((data) => data.date);
    }
 
    const data = {
        labels,
        datasets: [
            {
                label: "긍정",
                data: sentimentData.map((data) => data.positive),
                borderColor: "rgb(63, 102, 218)",
                backgroundColor: "rgba(63, 102, 218, 0.5)",
            },
            {
                label: "중립",
                data: sentimentData.map((data) => data.neutral),
                borderColor: "rgb(251, 196, 0)",
                backgroundColor: "rgba(251, 196, 0, 0.5)",
            },
            {
                label: "중립",
                data: sentimentData.map((data) => data.negative),
                borderColor: "rgb(255, 74, 111)",
                backgroundColor: "rgba(255, 74, 111, 0.5)",
            },
        ],
    };
    return (
        <div style={{height: "500px"}}>
            {sentimentData.length > 0 && <Line options={options} data={data} />}
        </div>
    );
}
 
export default LineChart;