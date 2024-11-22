class Questions:
    battery_questions = [
        "Does the vehicle fail to start when the start button is pressed?",
        "Does the battery take longer than usual to fully charge?",
        "Is the battery level dropping rapidly during use?",
        "Is the charging port unresponsive when the cable is connected?",
        "Is there an error message related to the battery on the display?"
    ]

    short_battery_questions = [
        "fail_start",
        "long_charge",
        "rapid_battery_drop",
        "unresponsive_charging_port",
        "battery_error_message"
    ]

    motor_questions = [
        "Is the motor making unusual noises when accelerating?",
        "Does the vehicle lose power suddenly while driving?",
        "Do you feel unusual vibrations while driving?",
        "Is the motor frequently overheating?",
        "Is the motor performance below expectations?"
    ]

    short_motor_questions = [
        "motor_noises",
        "power_loss",
        "driving_vibrations",
        "motor_overheat",
        "low_motor_performance"
    ]

    braking_questions = [
        "Is the regenerative braking system not working properly?",
        "Is there a loss of efficiency in energy regeneration when braking?",
        "Does the vehicle slide more than usual when braking?",
        "Do you hear unusual noises when braking?",
        "Is the brake pedal harder than normal?"
    ]

    short_braking_questions = [
        "regen_brake_issue",
        "low_regen_efficiency",
        "sliding_when_braking",
        "brake_noises",
        "brake_pedal_issue"
    ]

    electronics_questions = [
        "Is the main display or touch controls unresponsive?",
        "Do the internal or external lights flicker or fail intermittently?",
        "Are the proximity sensors not detecting obstacles correctly?",
        "Is the air conditioning or heating system not functioning?",
        "Is the GPS or navigation system showing frequent errors?"
    ]

    short_electronics_questions = [
        "unresponsive_display",
        "light_flicker",
        "sensor_malfunction",
        "ac_heating_issue",
        "gps_errors"
    ]

    tires_suspension_questions = [
        "Do the tires frequently lose pressure?",
        "Is the vehicle leaning to one side when parked?",
        "Do you feel instability when driving straight?",
        "Is the electric power steering system malfunctioning?",
        "Do you hear clunks or creaks when going over bumps?"
    ]

    short_tires_suspension_questions = [
        "frequent_tire_pressure_loss",
        "vehicle_leaning",
        "driving_instability",
        "steering_malfunction",
        "suspension_noises"
    ]

    software_questions = [
        "Are there pending software updates for the vehicle?",
        "Has there recently been a failure during a system update?",
        "Is the autonomous driving mode unresponsive or disconnecting randomly?",
        "Are there recurring maintenance alerts on the dashboard?",
        "Is the driving history displaying incorrect data?"
    ]

    short_software_questions = [
        "pending_updates",
        "update_failure",
        "autonomous_disconnect",
        "recurring_alerts",
        "incorrect_driving_history"
    ]

    misc_questions = [
        "Does the battery not reach its optimal operating temperature?",
        "Have you noticed an increase in the vehicle's energy consumption?",
        "Has the vehicle been exposed to extreme temperatures recently?",
        "Has any component of the vehicle been replaced recently?",
        "Has the vehicle been involved in an accident or minor impact?"
    ]

    short_misc_questions = [
        "battery_temp_issue",
        "high_energy_consumption",
        "extreme_temp_exposure",
        "recent_component_replacement",
        "minor_impact"
    ]

    @staticmethod
    def combine_questions(selected_categories):
        questions_complete = []
        short_questions_complete = []
        
        if 'battery' in selected_categories:
            questions_complete.extend(Questions.battery_questions)
            short_questions_complete.extend(Questions.short_battery_questions)
        if 'motor' in selected_categories:
            questions_complete.extend(Questions.motor_questions)
            short_questions_complete.extend(Questions.short_motor_questions)
        if 'braking' in selected_categories:
            questions_complete.extend(Questions.braking_questions)
            short_questions_complete.extend(Questions.short_braking_questions)
        if 'electronics' in selected_categories:
            questions_complete.extend(Questions.electronics_questions)
            short_questions_complete.extend(Questions.short_electronics_questions)
        if 'tires_suspension' in selected_categories:
            questions_complete.extend(Questions.tires_suspension_questions)
            short_questions_complete.extend(Questions.short_tires_suspension_questions)
        if 'software' in selected_categories:
            questions_complete.extend(Questions.software_questions)
            short_questions_complete.extend(Questions.short_software_questions)
        if 'misc' in selected_categories:
            questions_complete.extend(Questions.misc_questions)
            short_questions_complete.extend(Questions.short_misc_questions)
        
        return questions_complete, short_questions_complete