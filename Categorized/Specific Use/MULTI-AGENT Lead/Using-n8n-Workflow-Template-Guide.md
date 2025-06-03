# How to Use the n8n JSON Workflow Template for Your Automation Needs

This step-by-step guide will help you download, import, and use the JSON workflow template provided in your Gumroad purchase. Follow these instructions carefully to set up the workflows for scraping data, managing automation, and integrating multi-agent systems.

---

## **1. Prerequisites**

Before you begin, ensure you have the following:

- A **self-hosted n8n instance** or access to an n8n Cloud account.
- Basic knowledge of n8n workflows and nodes.
- API keys or credentials for:
  - **SERP API** for web scraping.
  - OpenAI API and/or other AI model API keys
  - Any other required services (e.g., Google Sheets).
- Your purchased JSON workflow template downloaded from Gumroad.

---

## **2. Download the Workflow Template**

1. After purchasing the workflow template on Gumroad, locate the **download link** in your email or Gumroad library.
2. Click the link and download the `.json` file to your local machine.

---

## **3. Import the JSON Workflow into n8n**

1. Log in to your n8n instance.
2. Click the **Import Workflow** button in the n8n editor (located in the top-right corner).
3. Choose the downloaded `.json` file and upload it.
4. Once imported, you will see the workflow appear in the editor.

---

## **4. Configure the Web Scraper Automation Workflow**

This workflow uses the SERP API to query Google Maps for businesses.

1. Open the **Web Scraper Workflow** node group.
2. Update the **SERP API Node** with your API key:
   - Navigate to the credentials section.
   - Add or update the SERP API credentials.
3. Customize the search parameters (e.g., `chelsea+london+real+estate`) as per your requirements.

---

## **5. Set Up the Google Sheets File**

The scraped data will be stored in Google Sheets:

1. Create a new Google Sheet in your Google Drive.
2. Update the **Google Sheets Node** in the workflow:
   - Provide the **Sheet ID** or file name.
   - Ensure you’ve authenticated the Google Sheets API with n8n.

---

## **6. Configure the Main Multi-Agent Web Crawler Workflow**

1. **Google Sheets Trigger**: Verify it’s correctly linked to your Google Sheets file containing URLs.
2. **Company Profile Data Scraper Agent**:
   - Ensure the website scraper node is configured to scrape relevant details.
3. **Social Media Links Scraper Agent**:
   - Update the logic to scrape URLs and social media profiles.
4. **Email Scraper Workflow**:
   - Check the email extraction node to ensure deduplication works as expected.

---

## **7. Connect Specialized Text and URL Scraper Workflows**

- **Text Scraper Workflow**:
  - Update the workflow to process text from website URLs.
  - Link the output to the Main Workflow.
- **URL Scraper Workflow**:
  - Extract valid URLs from the target sites.
  - Integrate its output into the Main Workflow.

---

## **8. Test the Workflow**

1. Click the **Test Workflow** button in the editor.
2. Use sample inputs (e.g., a small list of website URLs) to verify the process.
3. Check the outputs in:
   - Google Sheets for scraped data.
   - The n8n execution log for debugging information.

---

## **9. Adjust and Deploy the Workflow**

1. After successful testing, modify the workflow as needed to match your requirements.
2. Deploy the workflow:
   - Set up triggers for automated runs.
   - Schedule executions if necessary.

---

## **10. Maintain and Monitor**

1. Monitor the workflow logs for errors or performance issues.
2. Update API credentials and configurations periodically.

---

### **Support**

For any issues or questions, feel free to contact the Gumroad product support team or check the [n8n documentation](https://docs.n8n.io).

---

With these steps, you’ll be able to use the JSON workflow template to create robust automation systems effortlessly. Happy automating! 🚀
