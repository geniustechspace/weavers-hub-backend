if __name__ == "__main__":
    import uvicorn

    # Start Uvicorn server
    uvicorn.run(
        "weavers_hub_backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
        use_colors=True,
    )
