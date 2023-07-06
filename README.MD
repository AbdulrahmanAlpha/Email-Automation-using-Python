# Email Automation using Python

This is a Python script for automating the process of sending emails. With this script, you can schedule emails, format messages, personalize content, add attachments, and more.

## Installation

To use this script, you'll need to install the following libraries:

- `smtplib`
- `email`

You can install these libraries using pip:

```
pip install smtplib email
```

## Usage

To use this script, follow these steps:

1. Clone this repository to your local machine.
2. Open the `email_automation.py` file in your preferred text editor.
3. Update the following variables in the script:
   - `msg['Subject']`: Set the subject of the email message.
   - `msg['From']`: Set the email address of the sender.
   - `msg['To']`: Set the email address of the recipient.
   - `msg.set_payload()`: Set the content of the email message.
   - `attachment_path`: Set the path to the attachment file.
   - `server.login()`: Set the email address and password of the sender's email account.
   - `schedule.every().day.at()`: Set the time and frequency of the email sending.
4. Save the changes to the script.
5. Run the script using the following command:

```
python email_automation.py
```

The script will run in the background and send email messages according to the schedule you set.

## Contributing

If you find any bugs or issues with this script, please feel free to open an issue or submit a pull request.

## License

This script is licensed under the MIT License. See the LICENSE file for more information.