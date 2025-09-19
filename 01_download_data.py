#!/usr/bin/env python3
"""
Download SP 500 stocks dataset from Kaggle
"""

import kagglehub
import os
import shutil

def download_sp500_dataset():
    """Download and organize SP 500 stocks dataset"""
    print("🚀 Starting to download SP 500 stocks dataset...")
    
    try:
        # Download latest version
        path = kagglehub.dataset_download("andrewmvd/sp-500-stocks")
        print(f"✅ Dataset downloaded to: {path}")
        
        # Create data directory in project
        project_data_dir = "data"
        if not os.path.exists(project_data_dir):
            os.makedirs(project_data_dir)
            print(f"📁 Created data directory: {project_data_dir}")
        
        # Copy files to project data directory
        for file in os.listdir(path):
            src = os.path.join(path, file)
            dst = os.path.join(project_data_dir, file)
            shutil.copy2(src, dst)
            print(f"📋 Copied {file} to {project_data_dir}/")
        
        print(f"\n🎉 Dataset successfully downloaded and organized!")
        print(f"📍 Dataset files are available in: {os.path.abspath(project_data_dir)}")
        
        # List downloaded files
        print("\n📄 Downloaded files:")
        for file in os.listdir(project_data_dir):
            file_path = os.path.join(project_data_dir, file)
            size = os.path.getsize(file_path) / 1024  # KB
            print(f"  - {file} ({size:.1f} KB)")
            
    except Exception as e:
        print(f"❌ Error downloading dataset: {e}")
        print("💡 Make sure you have Kaggle API credentials configured.")
        print("   See: https://github.com/Kaggle/kaggle-api#api-credentials")

if __name__ == "__main__":
    download_sp500_dataset()
