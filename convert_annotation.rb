require 'rexml/document'

Dir.glob('Annotations/*.xml').each do |path|
  f = File.new path
  doc = REXML::Document.new f

  # Get Image path
  imgpath = File.absolute_path(
    File.join('TrainImages',
              File.basename(path, '.xml') + '.jpg')
  )

  # Check if Image file exists
  raise Errno::ENOENT unless File.exist? imgpath

  # Get Boxes
  boxes = doc.get_elements('//annotation/object/bndbox').map do |box|
    box = %w[xmin ymin xmax ymax].map do |name|
      box.elements[name].text.to_i
    end
    box[0] = (box[0] * 416.0 / 565.0).to_i
    box[2] = (box[2] * 416.0 / 565.0).to_i
    box[1] = (box[1] * 416.0 / 485.0).to_i
    box[3] = (box[3] * 416.0 / 485.0).to_i
    box << 0 # This time, Polyp class only.
  end

  puts imgpath + ' ' + boxes.map { |i| i.join(',') }.join(' ')
end
