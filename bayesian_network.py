from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

class BNetwork:
    def __init__(self):
        self.model = BayesianNetwork([
            ('fail_start', 'BatteryIssue'),
            ('long_charge', 'BatteryIssue'),
            ('rapid_battery_drop', 'BatteryIssue'),
            ('unresponsive_charging_port', 'BatteryIssue'),
            ('battery_error_message', 'BatteryIssue'),
            ('motor_noises', 'MotorIssue'),
            ('power_loss', 'MotorIssue'),
            ('driving_vibrations', 'MotorIssue'),
            ('motor_overheat', 'MotorIssue'),
            ('low_motor_performance', 'MotorIssue'),
            ('regen_brake_issue', 'BrakingIssue'),
            ('low_regen_efficiency', 'BrakingIssue'),
            ('sliding_when_braking', 'BrakingIssue'),
            ('brake_noises', 'BrakingIssue'),
            ('brake_pedal_issue', 'BrakingIssue'),
            ('unresponsive_display', 'ElectronicsIssue'),
            ('light_flicker', 'ElectronicsIssue'),
            ('sensor_malfunction', 'ElectronicsIssue'),
            ('ac_heating_issue', 'ElectronicsIssue'),
            ('gps_errors', 'ElectronicsIssue'),
            ('frequent_tire_pressure_loss', 'TiresSuspensionIssue'),
            ('vehicle_leaning', 'TiresSuspensionIssue'),
            ('driving_instability', 'TiresSuspensionIssue'),
            ('steering_malfunction', 'TiresSuspensionIssue'),
            ('suspension_noises', 'TiresSuspensionIssue'),
            ('pending_updates', 'SoftwareIssue'),
            ('update_failure', 'SoftwareIssue'),
            ('autonomous_disconnect', 'SoftwareIssue'),
            ('recurring_alerts', 'SoftwareIssue'),
            ('incorrect_driving_history', 'SoftwareIssue'),
            ('battery_temp_issue', 'MiscIssue'),
            ('high_energy_consumption', 'MiscIssue'),
            ('extreme_temp_exposure', 'MiscIssue'),
            ('recent_component_replacement', 'MiscIssue'),
            ('minor_impact', 'MiscIssue')
        ])
        
        cpd_battery_issue = TabularCPD(
            variable='BatteryIssue',
            variable_card=2,
            values=[
                [0.99, 0.95, 0.90, 0.85, 0.80, 0.75, 0.70, 0.65, 0.60, 0.55, 0.50, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.04, 0.03, 0.02, 0.01, 0.005, 0.004, 0.003, 0.002, 0.001, 0.0005, 0.0004, 0.0001],
                [0.01, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.96, 0.97, 0.98, 0.99, 0.995, 0.996, 0.997, 0.998, 0.999, 0.9995, 0.9996, 0.9999]
            ],
            evidence=['fail_start', 'long_charge', 'rapid_battery_drop', 'unresponsive_charging_port', 'battery_error_message'],
            evidence_card=[2, 2, 2, 2, 2]
        )

        cpd_motor_issue = TabularCPD(
            variable='MotorIssue',
            variable_card=2,
            values=[
                [0.99, 0.95, 0.90, 0.85, 0.80, 0.75, 0.70, 0.65, 0.60, 0.55, 0.50, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.04, 0.03, 0.02, 0.01, 0.005, 0.004, 0.003, 0.002, 0.001, 0.0005, 0.0004, 0.0001],
                [0.01, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.96, 0.97, 0.98, 0.99, 0.995, 0.996, 0.997, 0.998, 0.999, 0.9995, 0.9996, 0.9999]
            ],
            evidence=['motor_noises', 'power_loss', 'driving_vibrations', 'motor_overheat', 'low_motor_performance'],
            evidence_card=[2, 2, 2, 2, 2]
        )

        cpd_braking_issue = TabularCPD(
            variable='BrakingIssue',
            variable_card=2,
            values=[
                [0.83, 0.72, 0.63, 0.54, 0.50, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.04, 0.03, 0.02, 0.01, 0.005, 0.004, 0.003, 0.002, 0.001, 0.0005, 0.0004, 0.0003, 0.0002, 0.0001, 0.00005, 0.00004, 0.00003, 0.00001],
                [0.17, 0.28, 0.37, 0.46, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.96, 0.97, 0.98, 0.99, 0.995, 0.996, 0.997, 0.998, 0.999, 0.9995, 0.9996, 0.9997, 0.9998, 0.9999, 0.99995, 0.99996, 0.99997, 0.99999]
            ],
            evidence=['regen_brake_issue', 'low_regen_efficiency', 'sliding_when_braking', 'brake_noises', 'brake_pedal_issue'],
            evidence_card=[2, 2, 2, 2, 2]
        )

        cpd_electronics_issue = TabularCPD(
            variable='ElectronicsIssue',
            variable_card=2,
            values=[
                [0.73, 0.62, 0.53, 0.44, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.04, 0.03, 0.02, 0.01, 0.005, 0.004, 0.003, 0.002, 0.001, 0.0005, 0.0004, 0.0003, 0.0002, 0.0001, 0.00005, 0.00004, 0.00003, 0.00002, 0.00001, 0.000005],
                [0.27, 0.38, 0.47, 0.56, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.96, 0.97, 0.98, 0.99, 0.995, 0.996, 0.997, 0.998, 0.999, 0.9995, 0.9996, 0.9997, 0.9998, 0.9999, 0.99995, 0.99996, 0.99997, 0.99998, 0.99999, 0.999995]
            ],
            evidence=['unresponsive_display', 'light_flicker', 'sensor_malfunction', 'ac_heating_issue', 'gps_errors'],
            evidence_card=[2, 2, 2, 2, 2]
        )   

        cpd_tires_suspension_issue = TabularCPD(
            variable='TiresSuspensionIssue',
            variable_card=2,
            values=[
                [0.88, 0.77, 0.68, 0.57, 0.50, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.04, 0.03, 0.02, 0.01, 0.005, 0.004, 0.003, 0.002, 0.001, 0.0005, 0.0004, 0.0003, 0.0002, 0.0001, 0.00005, 0.00004, 0.00003, 0.00001],
                [0.12, 0.23, 0.32, 0.43, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.96, 0.97, 0.98, 0.99, 0.995, 0.996, 0.997, 0.998, 0.999, 0.9995, 0.9996, 0.9997, 0.9998, 0.9999, 0.99995, 0.99996, 0.99997, 0.99999]
            ],
            evidence=['frequent_tire_pressure_loss', 'vehicle_leaning', 'driving_instability', 'steering_malfunction', 'suspension_noises'],
            evidence_card=[2, 2, 2, 2, 2]
        )

        cpd_software_issue = TabularCPD(
            variable='SoftwareIssue',
            variable_card=2,
            values=[
                [0.78, 0.67, 0.58, 0.49, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.04, 0.03, 0.02, 0.01, 0.005, 0.004, 0.003, 0.002, 0.001, 0.0005, 0.0004, 0.0003, 0.0002, 0.0001, 0.00005, 0.00004, 0.00003, 0.00002, 0.00001],
                [0.22, 0.33, 0.42, 0.51, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.96, 0.97, 0.98, 0.99, 0.995, 0.996, 0.997, 0.998, 0.999, 0.9995, 0.9996, 0.9997, 0.9998, 0.9999, 0.99995, 0.99996, 0.99997, 0.99998, 0.99999]
            ],
            evidence=['pending_updates', 'update_failure', 'autonomous_disconnect', 'recurring_alerts', 'incorrect_driving_history'],
            evidence_card=[2, 2, 2, 2, 2]
        )

        cpd_misc_issue = TabularCPD(
            variable='MiscIssue',
            variable_card=2,
            values=[
                [0.88, 0.77, 0.68, 0.57, 0.50, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.04, 0.03, 0.02, 0.01, 0.005, 0.004, 0.003, 0.002, 0.001, 0.0005, 0.0004, 0.0003, 0.0002, 0.0001, 0.00005, 0.00004, 0.00003, 0.00002],
                [0.12, 0.23, 0.32, 0.43, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 0.96, 0.97, 0.98, 0.99, 0.995, 0.996, 0.997, 0.998, 0.999, 0.9995, 0.9996, 0.9997, 0.9998, 0.9999, 0.99995, 0.99996, 0.99997, 0.99998]
            ],
            evidence=['battery_temp_issue', 'high_energy_consumption', 'extreme_temp_exposure', 'recent_component_replacement', 'minor_impact'],
            evidence_card=[2, 2, 2, 2, 2]
        )


        cpd_fail_start = TabularCPD('fail_start', variable_card=2,
                                     values=[[0.6], [0.4]],
                                       )
        
        cpd_long_charge = TabularCPD('long_charge', variable_card=2, 
                                    values=[[0.7], [0.3]],
                                    )

        cpd_rapid_battery_drop = TabularCPD('rapid_battery_drop', variable_card=2, 
                                            values=[[0.8], [0.2]],
                                            )

        cpd_unresponsive_charging_port = TabularCPD('unresponsive_charging_port', variable_card=2, 
                                                    values=[[0.5], [0.5]],
                                                    )

        cpd_battery_error_message = TabularCPD('battery_error_message', variable_card=2, 
                                            values=[[0.6], [0.4]],
                                            )

        cpd_motor_noises = TabularCPD('motor_noises', variable_card=2, 
                              values=[[0.6], [0.4]],
                              )

        cpd_power_loss = TabularCPD('power_loss', variable_card=2, 
                                    values=[[0.7], [0.3]],
                                    )

        cpd_driving_vibrations = TabularCPD('driving_vibrations', variable_card=2, 
                                            values=[[0.5], [0.5]],
                                            )

        cpd_motor_overheat = TabularCPD('motor_overheat', variable_card=2, 
                                        values=[[0.6], [0.4]],
                                        )

        cpd_low_motor_performance = TabularCPD('low_motor_performance', variable_card=2, 
                                            values=[[0.7], [0.3]],
                                            )

        cpd_regen_brake_issue = TabularCPD('regen_brake_issue', variable_card=2, 
                                   values=[[0.6], [0.4]],
                                   )

        cpd_low_regen_efficiency = TabularCPD('low_regen_efficiency', variable_card=2, 
                                            values=[[0.7], [0.3]],
                                            )

        cpd_sliding_when_braking = TabularCPD('sliding_when_braking', variable_card=2, 
                                            values=[[0.5], [0.5]],
                                            )

        cpd_brake_noises = TabularCPD('brake_noises', variable_card=2, 
                                    values=[[0.6], [0.4]],
                                    )

        cpd_brake_pedal_issue = TabularCPD('brake_pedal_issue', variable_card=2, 
                                        values=[[0.7], [0.3]],
                                        )

        cpd_unresponsive_display = TabularCPD('unresponsive_display', variable_card=2, 
                                      values=[[0.6], [0.4]],
                                      )

        cpd_light_flicker = TabularCPD('light_flicker', variable_card=2, 
                                    values=[[0.7], [0.3]],
                                    )

        cpd_sensor_malfunction = TabularCPD('sensor_malfunction', variable_card=2, 
                                            values=[[0.5], [0.5]],
                                            )

        cpd_ac_heating_issue = TabularCPD('ac_heating_issue', variable_card=2, 
                                        values=[[0.6], [0.4]],
                                        )

        cpd_gps_errors = TabularCPD('gps_errors', variable_card=2, 
                                    values=[[0.7], [0.3]],
                                    )

        cpd_frequent_tire_pressure_loss = TabularCPD('frequent_tire_pressure_loss', variable_card=2, 
                                             values=[[0.6], [0.4]],
                                             )

        cpd_vehicle_leaning = TabularCPD('vehicle_leaning', variable_card=2, 
                                        values=[[0.5], [0.5]],
                                        )

        cpd_driving_instability = TabularCPD('driving_instability', variable_card=2, 
                                            values=[[0.6], [0.4]],
                                            )

        cpd_steering_malfunction = TabularCPD('steering_malfunction', variable_card=2, 
                                            values=[[0.7], [0.3]],
                                            )

        cpd_suspension_noises = TabularCPD('suspension_noises', variable_card=2, 
                                        values=[[0.6], [0.4]],
                                        )

        cpd_pending_updates = TabularCPD('pending_updates', variable_card=2, 
                                  values=[[0.7], [0.3]],
                                  )

        cpd_update_failure = TabularCPD('update_failure', variable_card=2, 
                                        values=[[0.6], [0.4]],
                                        )

        cpd_autonomous_disconnect = TabularCPD('autonomous_disconnect', variable_card=2, 
                                            values=[[0.5], [0.5]],
                                            )

        cpd_recurring_alerts = TabularCPD('recurring_alerts', variable_card=2, 
                                        values=[[0.6], [0.4]],
                                        )

        cpd_incorrect_driving_history = TabularCPD('incorrect_driving_history', variable_card=2, 
                                                values=[[0.7], [0.3]],
                                                )  

        cpd_battery_temp_issue = TabularCPD('battery_temp_issue', variable_card=2, 
                                    values=[[0.6], [0.4]],
                                    )

        cpd_high_energy_consumption = TabularCPD('high_energy_consumption', variable_card=2, 
                                                values=[[0.7], [0.3]],
                                                )

        cpd_extreme_temp_exposure = TabularCPD('extreme_temp_exposure', variable_card=2, 
                                            values=[[0.6], [0.4]],
                                            )

        cpd_recent_component_replacement = TabularCPD('recent_component_replacement', variable_card=2, 
                                                    values=[[0.6], [0.4]],
                                                    )

        cpd_minor_impact = TabularCPD('minor_impact', variable_card=2, 
                                    values=[[0.5], [0.5]],
                                    )
      

        # Add CPDs to the model
        self.model.add_cpds(
            cpd_battery_issue, cpd_motor_issue, cpd_braking_issue, cpd_electronics_issue, cpd_tires_suspension_issue,
            cpd_software_issue, cpd_misc_issue, cpd_fail_start, cpd_long_charge, cpd_rapid_battery_drop,
            cpd_unresponsive_charging_port, cpd_battery_error_message, cpd_motor_noises, cpd_power_loss,
            cpd_driving_vibrations, cpd_motor_overheat, cpd_low_motor_performance, cpd_regen_brake_issue,
            cpd_low_regen_efficiency, cpd_sliding_when_braking, cpd_brake_noises, cpd_brake_pedal_issue,
            cpd_unresponsive_display, cpd_light_flicker, cpd_sensor_malfunction, cpd_ac_heating_issue, cpd_gps_errors,
            cpd_frequent_tire_pressure_loss, cpd_vehicle_leaning, cpd_driving_instability, cpd_steering_malfunction,
            cpd_suspension_noises, cpd_pending_updates, cpd_update_failure, cpd_autonomous_disconnect,
            cpd_recurring_alerts, cpd_incorrect_driving_history, cpd_battery_temp_issue, cpd_high_energy_consumption,
            cpd_extreme_temp_exposure, cpd_recent_component_replacement, cpd_minor_impact
        )

    def infer(self):
        inference = VariableElimination(self.model)
        return inference