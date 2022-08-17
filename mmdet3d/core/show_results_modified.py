from os import path as osp
import mmcv
import numpy as np

def show_results_modified(points,
                          gt_bboxes,
                          pred_bboxes,
                          show=False,
                          out_dir=None,
                          filename=None):
    """Convert results into format that is directly readable for meshlab.

    Args:
        points (np.ndarray): Points.
        gt_bboxes (np.ndarray): Ground truth boxes.
        pred_bboxes (np.ndarray): Predicted boxes.
        show (bool, optional): Visualize the results on screen. Defaults to False.
        out_dir (str): Path of output directory
        filename (str): Filename of the current frame.
    """
    from mmdet3d.core.visualizer.open3d_vis import Visualizer
    vis = Visualizer(points, show=show)

    # Define path to save images to
    if filename is not None:
        result_path = out_dir
        mmcv.mkdir_or_exist(result_path)
        show_path = osp.join(result_path, f'{filename}_online.png')
    else:
        show_path = None

    # Display Predicted Bounding Box
    vis.add_bboxes(bbox3d=pred_bboxes)

    # Display Ground Truth Boudning Box
    vis.add_bboxes(bbox3d=gt_bboxes, bbox_color=(0, 0, 1))
    
    # Display results to screen
    if show:
        vis.show(show_path)
    else:
        vis.show_no_display(show_path)