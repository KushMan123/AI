import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const Navbar = (props) => {
	return (
		<nav>
			<ul>
				<li>
					<div class='logo'>
						<span class='nav-item green'>MEDICAL BOT</span>
					</div>
				</li>
				<li>
					<div
						onClick={() => {
							props.handleFunction();
						}}>
						<i class='fas fa-menorah'></i>
						<span class='nav-item'>Dashboard</span>
					</div>
				</li>
				<li>
					<div>
						<i class='fas fa-comment'></i>
						<span class='nav-item'>Patient Report</span>
					</div>
				</li>
			</ul>
		</nav>
	);
};

export default Navbar;
