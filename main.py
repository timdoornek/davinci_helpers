from python_get_resolve import GetResolve
import import_operations
import comp_operations
from pprint import pprint

if __name__ == '__main__':
    # app is injected dynamically by Davinci
    resolve = app.GetResolve()
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    fusion = resolve.Fusion()

    import_operations.add_videos_to_media_pool(resolve)
    import_operations.add_videos_to_timeline_from_media_pool(project)
    comp_operations.adding_home_run_comp(project)
