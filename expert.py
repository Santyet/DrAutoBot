from experta import KnowledgeEngine, Rule, Fact
from bayesian_network import BNetwork

class Symptom(Fact):
    """Info about the car's symptoms."""
    pass

class CarDiagnostic(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.diagnoses = {}
        self.bayesian_network = BNetwork()

    def reset(self):
        self.diagnoses = {}
        self._facts = {}
        self._agenda = []
        self._rules = []
        self._rule_facts = {}
        self._rule_agenda = {}
        self._rule_fired = {}
        self._rule_fired_count = 0

    def add_diagnosis(self, percentage, diagnosis, suggestion):
        if diagnosis not in self.diagnoses:
            self.diagnoses[diagnosis] = []
        self.diagnoses[diagnosis].append(f"{percentage}\n{suggestion}")

    # Reglas para síntomas individuales
    @Rule(Symptom(fail_start=True))
    def battery_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['BatteryIssue'], evidence={'fail_start': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of battery issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Battery issue causing failure to start.",
            "• Suggestion: Check the battery connections and charge or replace the battery if necessary."
        )

    @Rule(Symptom(long_charge=True))
    def long_charge_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['BatteryIssue'], evidence={'long_charge': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of long charge issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Battery issue causing long charge times.",
            "• Suggestion: Check the battery and charging system for issues."
        )

    @Rule(Symptom(rapid_battery_drop=True))
    def rapid_battery_drop_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['BatteryIssue'], evidence={'rapid_battery_drop': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of rapid battery drop issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Rapid battery drop indicating potential battery degradation.",
            "• Suggestion: Inspect the battery for signs of wear and consider replacing it."
        )

    @Rule(Symptom(unresponsive_charging_port=True))
    def unresponsive_charging_port_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['BatteryIssue'], evidence={'unresponsive_charging_port': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of unresponsive charging port issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Unresponsive charging port indicating potential connection issues.",
            "• Suggestion: Check the charging port for debris and ensure a secure connection."
        )

    @Rule(Symptom(battery_error_message=True))
    def battery_error_message_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['BatteryIssue'], evidence={'battery_error_message': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of battery error message issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Battery error message indicating potential battery or charging system issues.",
            "• Suggestion: Perform a diagnostic test on the battery and charging system."
        )

    @Rule(Symptom(motor_noises=True))
    def motor_noises_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['MotorIssue'], evidence={'motor_noises': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of motor noises issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Motor noises indicating potential motor issues.",
            "• Suggestion: Inspect the motor for loose components or damage and perform a diagnostic test."
        )

    @Rule(Symptom(power_loss=True))
    def power_loss_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['MotorIssue'], evidence={'power_loss': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of power loss issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Power loss indicating potential motor or electrical issues.",
            "• Suggestion: Perform a diagnostic test on the motor and electrical system."
        )

    @Rule(Symptom(regen_brake_issue=True))
    def regen_brake_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['BrakingIssue'], evidence={'regen_brake_issue': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of regenerative brake issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Regenerative brake issue indicating potential problems with the regenerative braking system.",
            "• Suggestion: Inspect the regenerative braking system and perform a diagnostic test."
        )

    @Rule(Symptom(driving_vibrations=True))
    def driving_vibrations_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['MotorIssue'], evidence={'driving_vibrations': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of driving vibrations issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Driving vibrations indicating potential motor or suspension issues.",
            "• Suggestion: Inspect the motor and suspension system for loose components or damage."
        )

    @Rule(Symptom(motor_overheat=True))
    def motor_overheat_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['MotorIssue'], evidence={'motor_overheat': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of motor overheating issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Motor overheating indicating potential cooling system issues.",
            "• Suggestion: Check the motor cooling system and ensure proper airflow."
        )

    @Rule(Symptom(low_motor_performance=True))
    def low_motor_performance_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['MotorIssue'], evidence={'low_motor_performance': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of low motor performance issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Low motor performance indicating potential motor or electrical issues.",
            "• Suggestion: Perform a diagnostic test on the motor and electrical system."
        )

    @Rule(Symptom(unresponsive_display=True))
    def unresponsive_display_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['ElectronicsIssue'], evidence={'unresponsive_display': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of unresponsive display issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Unresponsive display indicating potential electronics issues.",
            "• Suggestion: Check the vehicle's electronic systems and perform a diagnostic test."
        )

    @Rule(Symptom(light_flicker=True))
    def light_flicker_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['ElectronicsIssue'], evidence={'light_flicker': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of light flicker issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Light flickering indicating potential electrical issues.",
            "• Suggestion: Inspect the vehicle's electrical system and check for loose connections."
        )

    @Rule(Symptom(sensor_malfunction=True))
    def sensor_malfunction_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['ElectronicsIssue'], evidence={'sensor_malfunction': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of sensor malfunction issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Sensor malfunction indicating potential electronics issues.",
            "• Suggestion: Perform a diagnostic test on the vehicle's sensors and electronic systems."
        )

    @Rule(Symptom(ac_heating_issue=True))
    def ac_heating_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['ElectronicsIssue'], evidence={'ac_heating_issue': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of AC/heating issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: AC/heating system issue indicating potential electronics or mechanical issues.",
            "• Suggestion: Check the AC/heating system and perform a diagnostic test."
        )

    @Rule(Symptom(suspension_noises=True))
    def suspension_noises_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['TiresSuspensionIssue'], evidence={'suspension_noises': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of suspension noises issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Suspension noises indicating potential suspension issues.",
            "• Suggestion: Inspect the suspension system for loose or damaged components."
        )

    @Rule(Symptom(steering_malfunction=True))
    def steering_malfunction_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['TiresSuspensionIssue'], evidence={'steering_malfunction': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of steering malfunction issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Electric power steering system malfunctioning.",
            "• Suggestion: Check the power steering fluid level and inspect the steering components."
        )

    @Rule(Symptom(pending_updates=True))
    def pending_updates_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['SoftwareIssue'], evidence={'pending_updates': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of pending updates issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Pending software updates for the vehicle.",
            "• Suggestion: Update the vehicle's software to the latest version."
        )

    @Rule(Symptom(update_failure=True))
    def update_failure_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['SoftwareIssue'], evidence={'update_failure': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of update failure issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Recent failure during a system update.",
            "• Suggestion: Retry the update or contact the manufacturer for support."
        )

    @Rule(Symptom(autonomous_disconnect=True))
    def autonomous_disconnect_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['SoftwareIssue'], evidence={'autonomous_disconnect': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of autonomous disconnect issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Autonomous driving mode unresponsive or disconnecting randomly.",
            "• Suggestion: Check for software updates and inspect the sensors."
        )

    @Rule(Symptom(recurring_alerts=True))
    def recurring_alerts_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['SoftwareIssue'], evidence={'recurring_alerts': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of recurring alerts issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Recurring maintenance alerts on the dashboard.",
            "• Suggestion: Perform a full diagnostic scan and address any issues found."
        )

    @Rule(Symptom(incorrect_driving_history=True))
    def incorrect_driving_history_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['SoftwareIssue'], evidence={'incorrect_driving_history': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of incorrect driving history issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Driving history displaying incorrect data.",
            "• Suggestion: Update the vehicle's software and check for any data corruption."
        )

    @Rule(Symptom(battery_temp_issue=True))
    def battery_temp_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['MiscIssue'], evidence={'battery_temp_issue': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of battery temperature issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Battery not reaching its optimal operating temperature.",
            "• Suggestion: Check the battery heating/cooling system."
        )

    @Rule(Symptom(high_energy_consumption=True))
    def high_energy_consumption_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['MiscIssue'], evidence={'high_energy_consumption': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of high energy consumption issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Increase in the vehicle's energy consumption.",
            "• Suggestion: Check the vehicle's energy usage and inspect for any power drains."
        )

    @Rule(Symptom(extreme_temp_exposure=True))
    def extreme_temp_exposure_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['MiscIssue'], evidence={'extreme_temp_exposure': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of issues due to extreme temperature exposure: {:.2f}%".format(prob * 100),
            "• Diagnosis: Issues caused by exposure to extreme temperatures.",
            "• Suggestion: Inspect the vehicle for any heat or cold-related damage and ensure all systems are functioning properly."
        )

    # Reglas compuestas
    @Rule(Symptom(fail_start=True) & Symptom(long_charge=True))
    def battery_and_charging_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['BatteryIssue'], evidence={'fail_start': 1, 'long_charge': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of battery and charging issue: {:.2f}%".format(prob * 100),
            "• Diagnosis: Battery issue causing failure to start and taking longer to charge.",
            "• Suggestion: Check the battery and charging system for issues."
        )

    @Rule(Symptom(motor_noises=True) & Symptom(power_loss=True))
    def motor_and_power_loss_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['MotorIssue'], evidence={'motor_noises': 1, 'power_loss': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of motor issue causing unusual noises and power loss: {:.2f}%".format(prob * 100),
            "• Diagnosis: Motor issue causing unusual noises and power loss.",
            "• Suggestion: Inspect the motor and electrical system for issues."
        )

    @Rule(Symptom(driving_vibrations=True) & Symptom(vehicle_leaning=True))
    def suspension_and_vibration_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['SuspensionIssue'], evidence={'driving_vibrations': 1, 'vehicle_leaning': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of suspension issues causing instability and vibrations while driving: {:.2f}%".format(prob * 100),
            "• Diagnosis: Suspension issues causing instability and vibrations while driving.",
            "• Suggestion: Inspect the suspension system and alignment."
        )

    @Rule(Symptom(unresponsive_display=True) & Symptom(light_flicker=True))
    def electronics_and_light_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['ElectronicsIssue'], evidence={'unresponsive_display': 1, 'light_flicker': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of electronics issue causing unresponsive display and light flickering: {:.2f}%".format(prob * 100),
            "• Diagnosis: Electronics issue causing unresponsive display and light flickering.",
            "• Suggestion: Check the vehicle's electrical system and update the software."
        )

    @Rule(Symptom(sensor_malfunction=True) & Symptom(ac_heating_issue=True))
    def sensor_and_ac_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['ElectronicsIssue'], evidence={'sensor_malfunction': 1, 'ac_heating_issue': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of electronics issue causing sensor malfunction and AC/heating system failure: {:.2f}%".format(prob * 100),
            "• Diagnosis: Sensor malfunction and AC/heating system not functioning.",
            "• Suggestion: Inspect the sensors and HVAC system for issues."
        )

    @Rule(Symptom(gps_errors=True) & Symptom(sensor_malfunction=True))
    def gps_and_sensor_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['ElectronicsIssue'], evidence={'gps_errors': 1, 'sensor_malfunction': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of electronics issue causing GPS errors and sensor malfunction: {:.2f}%".format(prob * 100),
            "• Diagnosis: GPS errors and sensor malfunction.",
            "• Suggestion: Update the GPS software and inspect the sensors for damage."
        )

    @Rule(Symptom(frequent_tire_pressure_loss=True) & Symptom(driving_instability=True))
    def tire_pressure_and_instability_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['TiresSuspensionIssue'], evidence={'frequent_tire_pressure_loss': 1, 'driving_instability': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of tire or suspension issue causing tire pressure loss and driving instability: {:.2f}%".format(prob * 100),
            "• Diagnosis: Frequent tire pressure loss causing driving instability.",
            "• Suggestion: Inspect the tires for punctures and check the alignment."
        )

    @Rule(Symptom(steering_malfunction=True) & Symptom(suspension_noises=True))
    def steering_and_suspension_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['TiresSuspensionIssue'], evidence={'steering_malfunction': 1, 'suspension_noises': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of tire or suspension issue causing steering malfunction and suspension noises: {:.2f}%".format(prob * 100),
            "• Diagnosis: Steering malfunction and suspension noises.",
            "• Suggestion: Inspect the steering and suspension components for wear or damage."
        )

    @Rule(Symptom(climate_control_noises=True) & Symptom(high_energy_consumption=True))
    def climate_control_and_energy_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['MiscIssue'], evidence={'climate_control_noises': 1, 'high_energy_consumption': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of miscellaneous issue causing climate control noises and high energy consumption: {:.2f}%".format(prob * 100),
            "• Diagnosis: Climate control noises and high energy consumption.",
            "• Suggestion: Check the HVAC system for blockages and perform a diagnostic scan."
        )

    @Rule(Symptom(recent_component_replacement=True) & Symptom(minor_impact=True))
    def component_replacement_and_impact_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['MiscIssue'], evidence={'recent_component_replacement': 1, 'minor_impact': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of miscellaneous issue due to recent component replacement and minor impact: {:.2f}%".format(prob * 100),
            "• Diagnosis: Issues related to recent component replacement and minor impact.",
            "• Suggestion: Inspect the replaced components for proper installation and check for any impact damage."
        )


    # Reglas compuestas adicionales para síntomas sin reglas específicas
    @Rule(Symptom(low_motor_performance=True) & Symptom(power_loss=True))
    def motor_performance_and_power_loss_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['MotorIssue'], evidence={'low_motor_performance': 1, 'power_loss': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of motor issue causing low performance and power loss: {:.2f}%".format(prob * 100),
            "• Diagnosis: Low motor performance and power loss indicating potential motor or electrical issues.",
            "• Suggestion: Perform a diagnostic test on the motor and electrical system."
        )

    @Rule(Symptom(brake_noises=True) & Symptom(brake_pedal_issue=True))
    def brake_noises_and_pedal_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['BrakeIssue'], evidence={'brake_noises': 1, 'brake_pedal_issue': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of brake issue causing noises and pedal problems: {:.2f}%".format(prob * 100),
            "• Diagnosis: Brake noises and pedal issues indicating potential brake system problems.",
            "• Suggestion: Inspect the brake pads, rotors, and fluid levels."
        )

    @Rule(Symptom(sliding_when_braking=True) & Symptom(low_regen_efficiency=True))
    def braking_and_regen_efficiency_issue(self):
        inference = self.bayesian_network.infer()
        bayes = inference.query(variables=['BrakeIssue'], evidence={'sliding_when_braking': 1, 'low_regen_efficiency': 1})
        prob = bayes.values[1]
        self.add_diagnosis(
            "• Probability of brake or regenerative system issue causing braking inefficiency: {:.2f}%".format(prob * 100),
            "• Diagnosis: Sliding when braking and low regenerative efficiency indicating potential brake or regenerative system issues.",
            "• Suggestion: Check the brake pads, rotors, and regenerative braking system."
        )
