from plyer import notification

notification.notify(title="Reminder",
                    message="Time for a break",
                    app_icon=None,
                    timeout=1200,
                    toast=False)
