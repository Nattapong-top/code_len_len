from moviepy.editor import VideoFileClip, vfx

# ตั้งค่าชื่อไฟล์
input_file = "input_video.avi"  # ชื่อไฟล์วิดีโอต้นฉบับของป๋า
output_file = "output_video.avi" # ชื่อไฟล์ที่จะบันทึกใหม่

# โหลดไฟล์วิดีโอ
clip = VideoFileClip(input_file)

# --- ปรับแต่งภาพ (แสงและสี) ---
# ปรับความสว่าง (Brightness): คูณ 1.2 คือสว่างขึ้น 20%
clip_bright = clip.fx(vfx.colorx, 1.2)

# ปรับความเข้มของสี (Saturation): คูณ 1.3 คือสีสดขึ้น 30%
# หมายเหตุ: ใน moviepy บางเวอร์ชันอาจต้องใช้การปรับสีด้วยวิธีอื่น แต่วิธีนี้พื้นฐานที่สุด
clip_colored = clip_bright.fx(vfx.lum_contrast, lum=0, contrast=0.1, contrast_thr=127) 
# หรือใช้ colorx ช่วยเร่งโทนสีโดยรวม

# --- ปรับแต่งเสียง ---
# เพิ่มความดังเสียง (Volume): คูณ 1.5 คือดังขึ้น 50%
final_clip = clip_colored.volumex(1.5)

# --- บันทึกไฟล์ใหม่ ---
print("กำลังประมวลผล... กรุณารอสักครู่")
# codec 'png' หรือ 'rawvideo' มักใช้กับ avi หรือใช้ 'libx264' สำหรับ mp4 จะขนาดเล็กกว่า
final_clip.write_videofile(output_file, codec='png', audio_codec='pcm_s16le')

print(f"เสร็จสิ้น! บันทึกไฟล์เป็น {output_file} เรียบร้อยครับ")