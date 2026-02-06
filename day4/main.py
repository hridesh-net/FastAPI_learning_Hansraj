from resume_extractor import process_resumes
from resume_analyzer import analyzing_pipeline


input_folder = "./Resumes"

if __name__ == "__main__":
    # Phase 1: Extract the content of resumes in markdown format
    md_list = process_resumes(input_folder)

    # Phase 2: Analyze the content of resumes using LLM and save the output in json file
    analyzing_pipeline(md_list)