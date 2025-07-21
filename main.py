import cv2
from line_follower import GreedyLineFollower

# Global variable to store the point clicked
clicked_point = None

def click_event(event, x, y, flags, param):
    global clicked_point
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_point = (x, y)
        print(f'Start point selected: {clicked_point}')
        cv2.waitKey(550)
        cv2.destroyAllWindows()

def main():
    global clicked_point

    # Load image
    image_name = "line1.png"
    img = cv2.imread(f'example_inputs/{image_name}')
    if img is None:
        print("Image not found. Make sure the path is correct.")
        return

    # Display image and wait for click
    cv2.imshow("Select Start Point", img)
    cv2.setMouseCallback("Select Start Point", click_event)
    print("Click a start point on the image...")
    cv2.waitKey(0)

    if not clicked_point:
        print("No point selected.")
        return

    # Convert image to grayscale for processing
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Run greedy path-finding with a dynamic threshold
    follower = GreedyLineFollower(color_threshold=125)               # adjust as needed
    path = follower.follow_line(clicked_point, gray_img)

    # Draw the path on the image with red dots
    for pt in path:
        cv2.circle(img, pt, 1, (0, 0, 255), -1)

    # Save and show result
    output_path = f'output/traced_{image_name}'
    cv2.imwrite(output_path, img)
    cv2.imshow("Traced Path", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(f'Path saved to {output_path}')

if __name__ == '__main__':
    main()