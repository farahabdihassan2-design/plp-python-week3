# Part A - Grade Reporter
scores = [72, 45, 90, 61, 38]

# Initialize variables for dynamic calculation
passed_count = 0
failed_count = 0
total_score = 0

# 1. Use a for loop to go through every score in the list
for score in scores:
    total_score += score
    
    # 2. Use if / elif / else to work out a grade
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    # 3. Print each score with its grade on its own line
    print(f"Score: {score} - Grade: {grade}")
    
    # 4. Count passes and fails
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

# 5. Calculate and print average, rounded to one decimal place
average = total_score / len(scores)

print(f"\nPassed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Average: {round(average, 1)}")