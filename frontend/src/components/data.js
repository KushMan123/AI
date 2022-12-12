import React from "react";
import Card from "./card";
import Database_svg from "./database_svg";
import Pill_svg from "./pills_svg";
import Stethoscope_svg from "./stethoscope-solid-svg";
import Syringe_svg from "./syringe-solid-svg";
import patientData from "../finaldata-1.json";
import sexData from "../diseaseAC.json";

const no_patients = Object.keys(patientData).length;
const no_DiseaseData = Object.keys(sexData).length;
const no_treatment=721;
const no_test=824;

const Data = () => {
	return (
		<div class='users'>
			<Card dataValue={no_patients} text='No. of Patient'>
				<Database_svg />
			</Card>
			<Card dataValue={no_DiseaseData} text='Total Disease '>
				<Pill_svg />
			</Card>
			<Card dataValue={no_treatment} text='Treatment Methodology'>
				<Stethoscope_svg />
			</Card>
			<Card dataValue={no_test} text='Test Methods'>
				<Syringe_svg />
			</Card>
		</div>
	);
};

export default Data;
