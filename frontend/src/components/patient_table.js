import React, { useEffect, useState } from "react";

const PatientTable = (props) => {
	useEffect(() => {
		console.log(props.data[7]["Age"]);
	});

	function handleFunction(e) {
		props.handleClick(e.target.getAttribute("data-id"));
	}

	return (
		<section class='attendance'>
			<div class='attendance-list'>
				<h1>Patient List</h1>
				<div class='table-section'>
					<table class='table'>
						<thead>
							<tr>
								<th>ID</th>
								<th>Age</th>
								<th>Sex</th>
								<th>Symptoms</th>
								<th>Pre-Medications</th>
								<th>Physical Examination</th>
								<th>Test</th>
								<th>Diagnosis</th>
								<th>Treatment</th>
							</tr>
						</thead>
						<tbody>
							{Object.keys(props.data).map((i) => {
								let age = props.data[i]["Age"];
								let symptoms = props.data[i]["Symptoms"];
								let sex = props.data[i]["Sex"];
								let pre_medication = props.data[i]["Pre_Medication"];
								let physical = props.data[i]["Physical Examination Results"];
								let tests = props.data[i]["Test"];
								let diagnosis = props.data[i]["Diagnosis"];
								let treatments = props.data[i]["Treatment"];
								return (
									<tr>
										<td>
											Patient#0{i}
											<button onClick={handleFunction} data-id={i}>
												More
											</button>
										</td>
										<td>{age !== null ? age.slice(0, 2) : age}</td>
										<td>{sex === "M" ? "Male" : "Female"}</td>
										<td>
											{symptoms.map((symptom, index) => {
												if (index < 4) {
													return (
														<ul>
															<li>{symptom}</li>
														</ul>
													);
												}
											})}
										</td>
										<td>
											{pre_medication.map((med, index) => {
												if (pre_medication.length === 0) {
													return (
														<ul>
															<li>-</li>
														</ul>
													);
												} else {
													return (
														<ul>
															<li>{med}</li>
														</ul>
													);
												}
											})}
										</td>
										<td>
											{Object.keys(physical).map((p) => {
												return (
													<ul>
														<li>
															{p}:{physical[p]}
														</li>
													</ul>
												);
											})}
										</td>
										<td>
											{tests.map((test, index) => {
												if (index < 4) {
													return (
														<ul>
															<li>{test}</li>
														</ul>
													);
												}
											})}
										</td>
										<td>
											{diagnosis.map((d, index) => {
												if (index < 4) {
													return (
														<ul>
															<li>{d}</li>
														</ul>
													);
												}
											})}
										</td>
										<td>
											{treatments.map((treatment, index) => {
												if (index < 4) {
													return (
														<ul>
															<li>{treatment}</li>
														</ul>
													);
												}
											})}
										</td>
									</tr>
								);
							})}
						</tbody>
					</table>
				</div>
			</div>
		</section>
	);
};

export default PatientTable;
