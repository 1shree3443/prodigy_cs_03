{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "943c0071",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "---------------- Password Complexity Checking Tool -----------------\n",
      "Enter your password: ········\n",
      "Entered Password: s###e\n",
      "\n",
      "Password Strength Level: Weak (None or only one criterion is met).\n",
      "\n",
      "Here are some quick tips for creating a secure password:\n",
      "1. Length: Aim for at least 12 characters.\n",
      "2. Mix Characters: Use a combination of uppercase, lowercase, numbers, and symbols.\n",
      "3. Avoid Common Words: Don't use easily guessable information.\n",
      "4. No Personal Info: Avoid using names, birthdays, or personal details.\n",
      "5. Use Passphrases: Consider combining multiple words or a sentence.\n",
      "6. Unique for Each Account: Don't reuse passwords across multiple accounts.\n",
      "7. Regular Updates: Change passwords periodically.\n",
      "8. Enable 2FA: Use Two-Factor Authentication where possible.\n",
      "9. Be Wary of Phishing: Avoid entering passwords on suspicious sites.\n",
      "10. Password Manager: Consider using one for secure and unique passwords.\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "import getpass\n",
    "\n",
    "print(\"---------------- Password Complexity Checking Tool -----------------\")\n",
    "\n",
    "def assess_password_strength(password):\n",
    "    # Checking criteria\n",
    "    has_numbers = any(char.isdigit() for char in password)\n",
    "    has_upper_lower_case = any(char.isupper() or char.islower() for char in password)\n",
    "    meets_length_requirement = len(password) >= 8\n",
    "    has_special_characters = bool(re.search(r\"[!@#$%^&*(),.?\\\":{}|<>]\", password))\n",
    "\n",
    "    # Counts the number of met criteria\n",
    "    met_criteria_count = sum([has_numbers, has_upper_lower_case, meets_length_requirement, has_special_characters])\n",
    "\n",
    "    # Classifies the password based on the number of met criteria\n",
    "    if met_criteria_count == 4:\n",
    "        return \"Password Strength Level: Very Strong (All criteria are met).\"\n",
    "    elif met_criteria_count == 3:\n",
    "        return \"Password Strength Level: Moderately Strong (Any 3 criteria are met).\"\n",
    "    elif met_criteria_count == 2:\n",
    "        return \"Password Strength Level: Strong (Any 2 criteria are met).\"\n",
    "    else:\n",
    "        return \"Password Strength Level: Weak (None or only one criterion is met).\"\n",
    "\n",
    "# Gets user input for the password without displaying it on the screen\n",
    "password_input = getpass.getpass(\"Enter your password: \")\n",
    "\n",
    "# Displayed characters as '#' except for the first and last character\n",
    "masked_password = password_input[0] + '#' * (len(password_input) - 2) + password_input[-1]\n",
    "\n",
    "# Assesses the password strength\n",
    "result = assess_password_strength(password_input)\n",
    "\n",
    "# Provides more specific feedback to the user\n",
    "print(\"Entered Password: {}\".format(masked_password))\n",
    "print(\"\")\n",
    "print(result)\n",
    "print(\"\")\n",
    "tips = [\n",
    "    \"Here are some quick tips for creating a secure password:\",\n",
    "    \"1. Length: Aim for at least 12 characters.\",\n",
    "    \"2. Mix Characters: Use a combination of uppercase, lowercase, numbers, and symbols.\",\n",
    "    \"3. Avoid Common Words: Don't use easily guessable information.\",\n",
    "    \"4. No Personal Info: Avoid using names, birthdays, or personal details.\",\n",
    "    \"5. Use Passphrases: Consider combining multiple words or a sentence.\",\n",
    "    \"6. Unique for Each Account: Don't reuse passwords across multiple accounts.\",\n",
    "    \"7. Regular Updates: Change passwords periodically.\",\n",
    "    \"8. Enable 2FA: Use Two-Factor Authentication where possible.\",\n",
    "    \"9. Be Wary of Phishing: Avoid entering passwords on suspicious sites.\",\n",
    "    \"10. Password Manager: Consider using one for secure and unique passwords.\"\n",
    "]\n",
    "\n",
    "# Displays the tips\n",
    "for tip in tips:\n",
    "    print(tip)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ced1ee90",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
