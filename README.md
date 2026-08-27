# Healthy Pipes — predicting pipeline failures

Hackathon solution by team **Mr. Sister**. An interactive maintenance-support system for oil-and-gas liquid pipeline networks that combines a physical flow model, a pipe-section model, and machine learning.

<img width="80%" alt="dashboard" src="https://github.com/Baltsat/users-when-repair/assets/42536677/e79c4b82-559f-4924-b56e-e1414c42fcab">

## What it does

For every section of the network the system reports:

-   Accumulated corrosion-driven wear.
-   Remaining service life.
-   Current risk of use, from a predictive model trained on historical downtime.
-   Forecast risk growth for that section.
-   Recommendations for changing operating regimes to extend service life, including what-if scenarios.

The network graph is rendered interactively with intuitive failure-probability markers. New data can be added through the interface, and the system is designed to be adapted to a live monitoring feed.

## Results

Extensive data analysis, many tested hypotheses, and several machine-learning models at different levels of interpretability. Model quality on 3-fold cross-validation, measured by F1, precision and recall, ranges from **0.91 to 0.99**.

## Data

Pipeline operating-regime telemetry: pressure, temperature, fluid flow, vibration.

## Project tasks

1. Prepare the data for model training.
2. Analyse the data and identify the features that drive pipeline failures.
3. Build and train a machine-learning model for failure prediction.
4. Evaluate model quality and run acceptance testing.
5. Build a user interface for visualising and monitoring pipeline condition.

## Stack

Python · Jupyter Notebook · pandas, numpy, scikit-learn · matplotlib, seaborn · CatBoost · Flask

## Install and run

1. Install Python and Git.
2. Clone the repository.
3. `pip install -r requirements.txt`
4. Run the notebooks for data processing and model training.
5. Start the web interface: `python main.py`

## Team

| Name | Role | Contact |
| --- | --- | --- |
| Vadim Olennikov | Data analysis and product | [t.me/LTDigor](https://t.me/LTDigor) |
| Sergey Vandanov | Machine learning and software engineering | [t.me/rapid76](https://t.me/rapid76) |
| Konstantin Baltsat | Machine learning | [t.me/baltsat](https://t.me/baltsat) |
