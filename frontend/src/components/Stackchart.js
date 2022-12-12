import React from "react";
import {
	Chart as ChartJS,
	CategoryScale,
	LinearScale,
	BarElement,
	Title,
	Tooltip,
	Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";
import d_data from "../diseaseAC.json";

ChartJS.register(
	CategoryScale,
	LinearScale,
	BarElement,
	Title,
	Tooltip,
	Legend
);

export const options = {
	plugins: {
		title: {
			display: true,
			text: "Chart.js Bar Chart - Stacked",
		},
	},
	responsive: true,
	scales: {
		x: {
			stacked: true,
		},
		y: {
			stacked: true,
		},
	},
};

const labels = Object.keys(d_data);

export const data = {
	labels,
	datasets: [
		{
			label: "0-20",
			data: Object.keys(d_data).map((i) => {
				console.log(d_data[i][1]);
				if (d_data[i][1] === [0, 20] && d_data[i][0] !== 0) {
					return {
						i: d_data[i][0],
					};
				}
			}),
			// data: labels.map(() => faker.datatype.number({ min: -1000, max: 1000 })),
			backgroundColor: "rgb(255, 99, 132)",
		},
		{
			label: "20-40",
			data: Object.keys(d_data).map((i) => {
				if (d_data[i][1] === [20, 40] && d_data[i][0] !== 0) {
					return {
						i: d_data[i][0],
					};
				}
			}),
			// data: labels.map(() => faker.datatype.number({ min: -1000, max: 1000 })),
			backgroundColor: "rgb(75, 192, 192)",
		},
		{
			label: "40-60",
			data: Object.keys(d_data).map((i) => {
				if (d_data[i][1] === [40, 60] && d_data[i][0] !== 0) {
					return {
						i: d_data[i][0],
					};
				}
			}),
			// data: labels.map(() => faker.datatype.number({ min: -1000, max: 1000 })),
			backgroundColor: "rgb(53, 162, 235)",
		},
		{
			label: "60-80",
			data: Object.keys(d_data).map((i) => {
				if (d_data[i][1] === [60, 80] && d_data[i][0] !== 0) {
					return {
						i: d_data[i][0],
					};
				}
			}),
			// data: labels.map(() => faker.datatype.number({ min: -1000, max: 1000 })),
			backgroundColor: "rgb(53, 162, 235)",
		},
		{
			label: "80-100",
			data: Object.keys(d_data).map((i) => {
				if (d_data[i][1] === [80, 100] && d_data[i][0] !== 0) {
					return {
						i: d_data[i][0],
					};
				}
			}),
			// data: labels.map(() => faker.datatype.number({ min: -1000, max: 1000 })),
			backgroundColor: "rgb(53, 162, 235)",
		},
	],
};

export default function StackedBarChart() {
	return <Bar options={options} data={data} width='1000px' height='400px' />;
}
