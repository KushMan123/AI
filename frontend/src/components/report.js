import React from "react";

const Report = (props) => {
	let age = props.data["Age"];
	let symptoms = props.data["Symptoms"];
	let sex = props.data["Sex"];
	let pre_medication = props.data["Pre_Medication"];
	let physical = props.data["Physical Examination Results"];
	let tests = props.data["Test"];
	let diagnosis = props.data["Diagnosis"];
	let treatments = props.data["Treatment"];
	return (
		<div class='wrapper'>
			<div class='left'>
				<h4>Patient ID: Patient#0{props.id}</h4>
				<p>Age: {age !== null ? age.slice(0, 2) : age}</p>
				<p>Sex: {sex === "M" ? "Male" : "Female"}</p>
			</div>
			<div class='right'>
				<div class='projects'>
					<h3>Symptoms</h3>
					<div class='projects_data'>
						<div class='data'>
							<p>{`${symptoms} `}</p>
						</div>
					</div>
				</div>
				<div class='projects'>
					<h3>Pre-medication</h3>
					<div class='projects_data'>
						<div class='data'>
							<p>
								{pre_medication.length !== 0
									? `${pre_medication}`
									: "No Pre-medication"}
							</p>
						</div>
					</div>
				</div>
				<div class='info'>
					<h3>Physical Examination</h3>
					<div class='info_data'>
						{Object.keys(physical).map((p) => {
							if(p!== "Height"){
								return (
									<div class='data'>
										<h4>{p}</h4>
										<p>{physical[p]}</p>
									</div>
								);
							}
							
						})}
					</div>
				</div>
				<div class='projects'>
					<h3>Test</h3>
					<div class='projects_data'>
						<div class='data'>
							<p>{`${tests} `}</p>
						</div>
					</div>
				</div>
				<div class='projects'>
					<h3>Diagnosis</h3>
					<div class='projects_data'>
						<div class='data'>
							<p>{`${diagnosis} `}</p>
						</div>
					</div>
				</div>
				<div class='projects'>
					<h3>Treatment</h3>
					<div class='projects_data'>
						<div class='data'>
							<p>{`${treatments} `}</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	);
};

export default Report;
