import React, { Fragment, useEffect, useState } from "react";
import ReactDOM from "react-dom/client";
import Navbar from "./navbar";
import Container from "../container/container";
import "../static/css/style.css";
import MainContainer from "../container/main-container";
import Data from "./data";
import PatientTable from "./patient_table";
import json from "../finaldata-1.json";
import { age, sex } from "../data/bar-data";
import Loading from "./Loading";
import Report from "./report";
import BarChart from "./Barchart";
import PieChart from "./PieChart";
import StackedBarChart from "./Stackchart";

function App() {
	const [data, setData] = useState([]);
	const [viewReport, setViewReport] = useState(false);
	const [id, setId] = useState(null);
	const [ageData, setAgeData] = useState({
		labels: Object.keys(age[0]),
		datasets: [
			{
				label: "Age Group",
				data: Object.keys(age[0]).map((data) => {
					return age[0][data];
				}),
			},
		],
		backgroundColor: [
			"rgba(75,192,192,1)",
			"#ecf0f1",
			"#50AF95",
			"#f3ba2f",
			"#2a71d0",
		],
		borderColor: "black",
		borderWidth: 2,
	});
	const [sexData, setSexData] = useState({
		labels: Object.keys(sex[0]),
		datasets: [
			{
				label: "Gender Composition",
				data: Object.keys(sex[0]).map((data) => {
					return sex[0][data];
				}),
			},
		],
		backgroundColor: [
			"rgba(75,192,192,1)",
			"#ecf0f1",
			"#50AF95",
			"#f3ba2f",
			"#2a71d0",
		],
		borderColor: "black",
		borderWidth: 2,
	});
	useEffect(() => {
		setData(json);
	});

	function ViewPatientReport(id) {
		console.log(id);
		setId(id);
		setViewReport(true);
	}

	function SetViewReportStatus() {
		setViewReport(true);
	}

	function RenderContent() {
		if (data.length === 0) {
			return (
				<Container>
					<Navbar handleFunction={SetViewReportStatus} />
					<MainContainer>
						<Loading LoadingText='Loading' />
					</MainContainer>
				</Container>
			);
		} else if (data.length !== 0 && !viewReport) {
			return (
				<Container>
					<Navbar handleFunction={SetViewReportStatus} />
					<MainContainer text='Dashboard'>
						<Data />
						<PatientTable data={data} handleClick={ViewPatientReport} />
						<div class='data_section'>
							<div class='main-top center'>
								<h1>Data Visualization</h1>
							</div>
							<div class='drawing'>
								<div class='piechart'>
									<div class='main-top center'>
										<h1>Sex Visualization</h1>
									</div>
									<PieChart chartData={sexData} />
								</div>
								<div class='barchart'>
									<div class='main-top center'>
										<h1>Age Visualization</h1>
									</div>
									<BarChart chartData={ageData} />
								</div>
							</div>
						</div>
					</MainContainer>
				</Container>
			);
		} else if (data.length !== 0 && viewReport) {
			return (
				<Container>
					<Navbar handleFunction={SetViewReportStatus} />
					<MainContainer text='Patient Report' secondClass='center'>
						<Report data={data[id]} id={id} />
					</MainContainer>
				</Container>
			);
		}
	}
	return <Fragment>{RenderContent()}</Fragment>;
}

const root = ReactDOM.createRoot(document.querySelector("#root"));
root.render(<App />);
