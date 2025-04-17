{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "83f8a3e8-5205-4138-ab6c-c301e1926b45",
   "metadata": {},
   "outputs": [],
   "source": [
    "# streamlit\n",
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b07cd030-2c0b-452c-9ee3-6c4bedb88ae0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-17 13:09:09.386 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-17 13:09:09.829 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\ProgramData\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-04-17 13:09:09.830 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-17 13:09:09.831 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-17 13:09:09.833 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-17 13:09:09.834 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-17 13:09:09.837 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-17 13:09:09.841 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "# Streamlit Interface\n",
    "st.title(\"🛒 Customer Conversion Analysis using Clickstream Data\")\n",
    "\n",
    "uploaded_file = st.file_uploader(\"Upload your CSV file\", type=[\"csv\"])\n",
    "\n",
    "if uploaded_file:\n",
    "    df1 = pd.read_csv(uploaded_file)\n",
    "    st.success(\"File Uploaded Successfully!\")\n",
    "\n",
    "    option = st.selectbox(\"Choose a Task\", [\"Classification\", \"Regression\", \"Clustering\"])\n",
    "\n",
    "    if option == \"Classification\":\n",
    "        model, metrics = train_classification_model(df1)\n",
    "        st.subheader(\"📈 Classification Results\")\n",
    "        for k, v in metrics.items():\n",
    "            st.write(f\"{k}: {v:.2f}\")\n",
    "\n",
    "    elif option == \"Regression\":\n",
    "        model, metrics = train_regression_model(df1)\n",
    "        st.subheader(\"📉 Regression Results\")\n",
    "        for k, v in metrics.items():\n",
    "            st.write(f\"{k}: {v:.2f}\")\n",
    "\n",
    "    elif option == \"Clustering\":\n",
    "        clustered_df, metrics = train_clustering_model(df1)\n",
    "        st.subheader(\"📊 Clustering Results\")\n",
    "        st.write(clustered_df.head())\n",
    "        for k, v in metrics.items():\n",
    "            st.write(f\"{k}: {v:.2f}\")"
   ]
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
